/*
 * mp2cn - Max Payne 2 全量字幕中文化注入层 (多字盘路线)
 *
 * 形态: 伪装成 dinput.dll 的代理 DLL，放进游戏目录即自动加载。
 *
 * 机制(关键): 游戏字幕在 .ras 里是 单字节高位编码 的中文
 *   (每个汉字 = 一个 0x80-0xFE 字节, 按 cn_map_v3 映射到烘焙字盘槽)。
 *   引擎按"单字节 -> 槽位"渲染, 传给 P_Text::print 的就是这串单字节。
 *
 * 本层:
 *   1) 把 dinput 的 7 个导出全部真实转发到 SysWOW64\dinput.dll
 *   2) 等 e2mfc.dll 加载后, 对 P_Text::print / executeAlways 装 inline hook
 *   3) print 里: 把传入的 单字节高位串 当"钥匙" (FNV-1a) 查 ALL_SUBS;
 *                命中 -> 整行替换成多字盘编码好的中文 (0x80+本盘槽), 记录盘号
 *   4) executeAlways 里: 若该对象有中文, 把字体指针换成对应中文字盘, 烘焙后还原
 *
 *   字盘按"一行必须同盘"装箱, 每张盘 128 汉字槽; 全量已译章节共 ALL_NDISKS 张。
 *   字盘懒加载(首次用到某盘时才构造 P_Font), 避免一次性加载几十张造成卡顿。
 */

#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdint.h>
#include <string.h>

#include "subs_all.h"      /* ALL_SUBS[], ALL_NDISKS */
#include "hist_trans.h"    /* HIST_TRANS_TABLE[] 旧编码->当前编码 (旧档兼容) */

/* ============================== 全局 ============================== */

static HMODULE          g_realDI = NULL;
static char             g_logPath[MAX_PATH];
static CRITICAL_SECTION g_lock;
static volatile LONG    g_lockReady = 0;

/* ============================== 日志(缓冲式, 绝不在渲染热路径做 fopen) ============================== */

#define LOG_BUF_CAP (1 << 16)   /* 64KB 缓冲 */
static char  g_logBuf[LOG_BUF_CAP];
static int   g_logLen = 0;
static int   g_logCalls = 0;

static void log_flush(void)
{
    if (!g_logPath[0] || g_logLen == 0) return;
    FILE *f = fopen(g_logPath, "ab");
    if (f) {
        fwrite(g_logBuf, 1, (size_t)g_logLen, f);
        fclose(f);
        g_logLen = 0;
    }
}

static void LOG(const char *fmt, ...)
{
    char  tmp[1024];
    int   n;
    va_list ap;

    if (!g_logPath[0]) return;
    va_start(ap, fmt);
    n = vsnprintf(tmp, sizeof(tmp), fmt, ap);
    va_end(ap);
    if (n <= 0) return;

    if (g_lockReady) EnterCriticalSection(&g_lock);
    if (g_logLen + n > (int)sizeof(g_logBuf)) log_flush();
    if (g_logLen + n <= (int)sizeof(g_logBuf)) {
        memcpy(g_logBuf + g_logLen, tmp, (size_t)n);
        g_logLen += n;
    }
    /* 每 64 次写盘一次: 避免崩溃丢太多, 也避免每次 fopen 拖慢渲染 */
    if ((++g_logCalls & 63) == 0) log_flush();
    if (g_lockReady) LeaveCriticalSection(&g_lock);
}

/* ==================== 文本去重（防日志爆炸） ==================== */

#define SEEN_CAP 16384
static uint32_t g_seen[SEEN_CAP];
static int      g_seenCount = 0;

static uint32_t fnv1a(const char *s)
{
    uint32_t h = 2166136261u;
    while (*s) { h ^= (unsigned char)*s++; h *= 16777619u; }
    return h ? h : 1u;
}

static uint32_t fnv1a_rtrim(const char *s)
{
    int len = (int)strlen(s);
    while (len > 0 && (s[len - 1] == ' ' || s[len - 1] == '\t')) len--;
    {
        uint32_t h = 2166136261u;
        int i;
        for (i = 0; i < len; i++) { h ^= (unsigned char)s[i]; h *= 16777619u; }
        return h ? h : 1u;
    }
}

static int seen_first_time(const char *s)
{
    uint32_t h;
    int      k;

    if (g_seenCount >= SEEN_CAP - 64) return 0;

    h = fnv1a(s);
    for (k = 0; k < SEEN_CAP; k++) {
        uint32_t j = (h + (uint32_t)k) % SEEN_CAP;
        if (g_seen[j] == 0) { g_seen[j] = h; g_seenCount++; return 1; }
        if (g_seen[j] == h) return 0;
    }
    return 0;
}

/* ======================== inline hook 引擎 ======================== */

static void *install_hook(void *target, void *detour, int stolen)
{
    BYTE  *tramp;
    BYTE   patch[32];
    DWORD  oldProt;
    int    i;

    if (!target || stolen < 5 || stolen > 24) return NULL;

    tramp = (BYTE *)VirtualAlloc(NULL, 64, MEM_COMMIT | MEM_RESERVE,
                                 PAGE_EXECUTE_READWRITE);
    if (!tramp) return NULL;

    memcpy(tramp, target, (size_t)stolen);
    tramp[stolen] = 0xE9;
    *(DWORD *)(tramp + stolen + 1) =
        (DWORD)((BYTE *)target + stolen) - ((DWORD)(tramp + stolen) + 5);

    for (i = 0; i < stolen; i++) patch[i] = 0x90;
    patch[0] = 0xE9;
    *(DWORD *)(patch + 1) = (DWORD)detour - ((DWORD)target + 5);

    if (!VirtualProtect(target, (SIZE_T)stolen, PAGE_EXECUTE_READWRITE, &oldProt)) {
        VirtualFree(tramp, 0, MEM_RELEASE);
        return NULL;
    }
    memcpy(target, patch, (size_t)stolen);
    VirtualProtect(target, (SIZE_T)stolen, oldProt, &oldProt);
    FlushInstructionCache(GetCurrentProcess(), target, (SIZE_T)stolen);

    return tramp;
}

/* ====================== e2mfc.dll 接口声明 ====================== */

typedef void         (__fastcall *print_t) (void *self, void *edx, const char *s);
typedef int          (__fastcall *exec_t) (void *self, void *edx);
typedef void *(__fastcall *ctor2_t)  (void *self, void *edx,
                                      const char *img, const char *alpha);

static print_t  o_print = NULL;
static exec_t   o_exec  = NULL;

#define SYM_PRINT    "?print@P_Text@@QAEXPBD@Z"
#define SYM_EXEC     "?executeAlways@P_Text@@MAE_NXZ"
#define SYM_FONTCTOR2 "??0P_Font@@QAE@PBD0@Z"

/* ===================== 中文字盘加载(懒加载) ===================== */

static void *g_myFonts[ALL_NDISKS];
static int   g_diskLoaded[ALL_NDISKS];   /* 0=未加载 1=已加载(成功或失败) */
static int   g_diskOk[ALL_NDISKS];        /* 1=字形体检通过 */
static volatile LONG g_fontsReady = 0;

static const char *const FONT_FORMS[] = {
    "..\\sharedtextures\\font_cn_%d.tga",
    "data\\sharedtextures\\font_cn_%d.tga",
    "data/sharedtextures/font_cn_%d.tga",
    "sharedtextures\\font_cn_%d.tga",
    "font_cn_%d.tga",
};

#define FONT_H_OFF   0x50
#define FONT_W_OFF   0x54
#define FONT_UV_OFF  0x454
#define FONT_STORE   0x4000

static char  g_fontStore[ALL_NDISKS][FONT_STORE];

static int load_one_disk(int d)
{
    ctor2_t p_fontCtor2;
    HMODULE e2 = GetModuleHandleA("e2mfc.dll");
    int     fi;

    if (!e2) return 0;
    p_fontCtor2 = (ctor2_t)GetProcAddress(e2, SYM_FONTCTOR2);
    if (!p_fontCtor2) return 0;

    for (fi = 0; fi < (int)(sizeof(FONT_FORMS)/sizeof(FONT_FORMS[0])); fi++) {
        char img[256], al[160];
        int  m;
        _snprintf(img, sizeof(img) - 16, FONT_FORMS[fi], d);
        m = (int)strlen(img);
        memcpy(al, img, m - 4);
        strcpy(al + m - 4, "_alpha.tga");

        p_fontCtor2(g_fontStore[d], 0, img, al);
        {
            int   fh   = *(const int *)(g_fontStore[d] + FONT_H_OFF);
            const int *wtab = (const int *)(g_fontStore[d] + FONT_W_OFF);
            /* 描边(2px)后引擎测得的字形高/宽会略增, 校验放宽(仍能挡掉错误文件) */
            if (fh >= 18 && fh <= 24 && wtab[0x80] >= 14 && wtab[0x80] <= 30) {
                g_myFonts[d] = g_fontStore[d];
                g_diskOk[d]  = 1;
                LOG("  ★ 盘%d 加载成功 (字高%d, 汉字宽%d)\n", d, fh, wtab[0x80]);
                return 1;
            }
        }
    }
    LOG("  !! 盘%d 所有候选都失败\n", d);
    return 0;
}

/* 懒加载: 首次用到盘 d 时构造。线程安全(每条盘只构造一次) */
static int ensure_disk(int d)
{
    if (d < 0 || d >= ALL_NDISKS) return 0;
    if (g_diskLoaded[d]) return g_diskOk[d];
    {
        static volatile LONG lock[ALL_NDISKS];
        if (InterlockedCompareExchange(&lock[d], 1, 0) == 0) {
            LOG("[ALL] 首次加载盘%d ...\n", d);
            g_diskOk[d]   = load_one_disk(d);
            g_diskLoaded[d] = 1;
        } else {
            /* 其他线程正在加载, 简单自旋等待 */
            int guard = 0;
            while (!g_diskLoaded[d] && guard++ < 1000) Sleep(1);
        }
    }
    return g_diskOk[d];
}

/* ===================== 对象 -> 字盘号 映射 ===================== */

#define PTRMAP_CAP 8192
static void* g_ptrKey[PTRMAP_CAP];
static int   g_ptrDisk[PTRMAP_CAP];

static void ptr_put(void *self, int disk)
{
    int k;
    uint32_t h = ((uint32_t)(uintptr_t)self) % PTRMAP_CAP;
    for (k = 0; k < PTRMAP_CAP; k++) {
        int j = (int)((h + k) % PTRMAP_CAP);
        if (g_ptrKey[j] == NULL || g_ptrKey[j] == self) {
            g_ptrKey[j] = self; g_ptrDisk[j] = disk; return;
        }
    }
}

static int ptr_get(void *self)
{
    int k;
    uint32_t h = ((uint32_t)(uintptr_t)self) % PTRMAP_CAP;
    for (k = 0; k < PTRMAP_CAP; k++) {
        int j = (int)((h + k) % PTRMAP_CAP);
        if (g_ptrKey[j] == NULL) return -1;
        if (g_ptrKey[j] == self) return g_ptrDisk[j];
    }
    return -1;
}

/* ===================== 字幕查表(高位字节钥匙) ===================== */

static int subs_lookup(const char *s, int *disk_out)
{
    uint32_t h = fnv1a_rtrim(s);
    int i;
    for (i = 0; ALL_SUBS[i].h != 0; i++) {
        if (ALL_SUBS[i].h == h) {
            *disk_out = ALL_SUBS[i].disk;
            return i;
        }
    }
    return -1;
}

/* 动态拼接串(如存档槽 "Mon, Aug 10 2026, 17:05 - 第五章 伏特加"): 整串查表必未命中。
 * 取字符串末尾最后一个连续高位字节段(=章节名部分)单独查表, 命中正确字盘。 */
static int subs_lookup_tailwide(const char *s, int *disk_out)
{
    int len = (int)strlen(s);
    int i;
    for (i = len - 1; i >= 0; i--) {
        if ((unsigned char)s[i] >= 0x80) {
            int start = i;
            while (start > 0 && (unsigned char)s[start - 1] >= 0x80) start--;
            {
                char tmp[512];
                int n = i - start + 1;
                if (n <= 0 || n >= (int)sizeof(tmp)) return -1;
                memcpy(tmp, s + start, (size_t)n);
                tmp[n] = 0;
                return subs_lookup(tmp, disk_out);
            }
        }
    }
    return -1;
}

/* 历史编码翻译(旧档兼容): 存档槽串的章节名编码可能是"旧版本"的(文本改动后装箱变化)。
 * 把尾部高位段按 HIST_TRANS_TABLE 翻译成当前编码, 重新查表。
 * 返回翻译后字符串(写入 out, 需调用方提供缓冲); 查表命中返回 >=0, 否则 -1。 */
static int subs_lookup_hist(const char *s, int *disk_out, char *out, int out_sz)
{
    int len = (int)strlen(s);
    int i, start, n, t;

    if (len <= 0) return -1;
    for (i = len - 1; i >= 0; i--)
        if ((unsigned char)s[i] >= 0x80) break;
    if (i < 0) return -1;
    start = i;
    while (start > 0 && (unsigned char)s[start - 1] >= 0x80) start--;
    n = i - start + 1;
    if (n <= 0) return -1;

    /* 尾部高位段 -> hex 串, 与翻译表比对 */
    {
        char hex[512];
        if (n * 2 + 1 > (int)sizeof(hex)) return -1;
        for (int k = 0; k < n; k++) {
            unsigned char b = (unsigned char)s[start + k];
            static const char *d = "0123456789abcdef";
            hex[k * 2]     = d[b >> 4];
            hex[k * 2 + 1] = d[b & 15];
        }
        hex[n * 2] = 0;

        for (t = 0; HIST_TRANS_TABLE[t].old_hex != NULL; t++) {
            if (strcmp(HIST_TRANS_TABLE[t].old_hex, hex) == 0) {
                const char *newhex = HIST_TRANS_TABLE[t].new_hex;
                int         newlen = HIST_TRANS_TABLE[t].new_len;
                if (start + newlen + 1 > out_sz) return -1;
                memcpy(out, s, (size_t)start);
                for (int k = 0; k < newlen; k++) {
                    int v1 = (newhex[k*2]   >= '0' && newhex[k*2]   <= '9') ? newhex[k*2]   - '0' :
                             (newhex[k*2]   >= 'a' && newhex[k*2]   <= 'f') ? newhex[k*2]   - 'a' + 10 : 0;
                    int v2 = (newhex[k*2+1] >= '0' && newhex[k*2+1] <= '9') ? newhex[k*2+1] - '0' :
                             (newhex[k*2+1] >= 'a' && newhex[k*2+1] <= 'f') ? newhex[k*2+1] - 'a' + 10 : 0;
                    out[start + k] = (char)((v1 << 4) | v2);
                }
                out[start + newlen] = 0;
                /* 完整翻译串(时间+新章节名)是动态拼接串, ALL_SUBS 只存静态串哈希;
                 * 必须对翻译后的串再取尾部高位段查表。 */
                return subs_lookup_tailwide(out, disk_out);
            }
        }
    }
    return -1;
}

static int   g_subHitLog = 0;
static int   g_subTotalHits = 0;

/* ===================== executeAlways hook ===================== */

static int __fastcall hk_exec(void *self, void *edx)
{
    void **slot  = (void **)((char *)self + 0x18C);   /* P_Font* */
    void  *saved = *slot;
    int    disk  = ptr_get(self);
    int    r;

    if (disk >= 0 && disk < ALL_NDISKS && ensure_disk(disk) && g_myFonts[disk]) {
        *slot = g_myFonts[disk];
        r = o_exec(self, edx);
        *slot = saved;
    } else {
        r = o_exec(self, edx);
    }
    return r;
}

/* ===================== print hook ===================== */

static void __fastcall hk_print(void *self, void *edx, const char *s)
{
    /* 方案B: 文本已是 .ras 里的高位中文, 本层只负责换字盘, 不替换文本。
     * 注意: 本函数运行在引擎渲染线程, 绝不可做任何阻塞 I/O(如 fopen),
     *       否则会卡住整帧(表现为读档界面鼠标卡顿数秒)。 */
    if (s && *s && g_fontsReady) {
        int has_wide = 0;
        for (const char *p = s; *p; p++)
            if ((unsigned char)*p >= 0x80) { has_wide = 1; break; }
        if (has_wide) {
            int disk = -1;
            int idx = subs_lookup(s, &disk);
            if (idx < 0) idx = subs_lookup_tailwide(s, &disk); /* 动态拼接串: 取末尾高位段(章节名)查表 */
            if (idx < 0) {
                /* 历史编码翻译: 旧档章节名编码 -> 当前编码, 再查表(兼容存档乱码) */
                static char histBuf[512];
                idx = subs_lookup_hist(s, &disk, histBuf, (int)sizeof(histBuf));
                if (idx >= 0) s = histBuf;   /* 用翻译后的串渲染 */
            }
            if (idx < 0) disk = 0;   /* 仍不命中才兜底盘0 */
            if (disk >= 0 && disk < ALL_NDISKS && ensure_disk(disk) && g_myFonts[disk]) {
                ptr_put(self, disk);
            }
        }
    }
    o_print(self, edx, s);
}

/* ===================== 等 e2mfc 加载并装钩子 ===================== */

static DWORD WINAPI init_thread(LPVOID unused)
{
    HMODULE e2 = NULL;
    void   *pPrint;
    int     i;

    (void)unused;

    for (i = 0; i < 1200; i++) {
        e2 = GetModuleHandleA("e2mfc.dll");
        if (e2) break;
        Sleep(100);
    }
    if (!e2) { LOG("[ERR] 超时: e2mfc.dll 始终未加载\n"); return 0; }

    LOG("[OK ] e2mfc.dll @ %p\n", (void *)e2);
    Sleep(800);

    pPrint = (void *)GetProcAddress(e2, SYM_PRINT);
    if (!pPrint) { LOG("[ERR] 找不到 P_Text::print\n"); return 0; }

    {
        static const BYTE expect[7] = { 0x51, 0x8B, 0x81, 0x88, 0x01, 0x00, 0x00 };
        const BYTE *b = (const BYTE *)pPrint;
        if (memcmp(pPrint, expect, 7) != 0) {
            LOG("[ERR] print 开头字节不符, 拒绝 hook\n");
            return 0;
        }
    }

    o_print = (print_t)install_hook(pPrint, (void *)hk_print, 7);
    if (!o_print) { LOG("[ERR] install_hook(print) 失败\n"); return 0; }
    LOG("[OK ] P_Text::print 已挂钩\n");

    {
        static const BYTE ex[5] = { 0x83, 0xEC, 0x30, 0x53, 0x55 };
        void *pExec = (void *)GetProcAddress(e2, SYM_EXEC);
        if (!pExec) {
            LOG("[ERR] 找不到 P_Text::executeAlways\n");
        } else if (memcmp(pExec, ex, 5) != 0) {
            LOG("[ERR] executeAlways 开头字节不符, 拒绝 hook\n");
        } else {
            o_exec = (exec_t)install_hook(pExec, (void *)hk_exec, 5);
            LOG("[OK ] P_Text::executeAlways 已挂钩\n");
        }
    }

    /* 字盘懒加载, 机制就绪即可开始匹配; 实际加载推迟到首次用到某盘 */
    g_fontsReady = 1;
    LOG("--------- [ALL] 全量字幕注入已就绪, 共 %d 条, %d 张字盘 (懒加载) ---------\n",
        (int)(sizeof(ALL_SUBS)/sizeof(ALL_SUBS[0]) - 1), ALL_NDISKS);
    return 0;
}

/* ================ dinput.dll 7 个导出的真实转发 ================ */

static void load_real_dinput(void)
{
    char sys[MAX_PATH];
    UINT n;

    if (g_realDI) return;
    n = GetSystemDirectoryA(sys, MAX_PATH);
    if (!n || n >= MAX_PATH - 16) return;
    strcat(sys, "\\dinput.dll");
    g_realDI = LoadLibraryA(sys);
    LOG("[DI ] 真 dinput = %s -> %p\n", sys, (void *)g_realDI);
}

#define FORWARD(rettype, name, proto, args)                                 \
    typedef rettype (WINAPI *pfn_##name) proto;                             \
    __declspec(dllexport) rettype WINAPI name proto {                       \
        static pfn_##name fn = NULL;                                        \
        if (!fn) {                                                          \
            load_real_dinput();                                             \
            if (g_realDI) fn = (pfn_##name)GetProcAddress(g_realDI, #name); \
        }                                                                   \
        if (!fn) return (rettype)0x80004005L;                               \
        return fn args;                                                     \
    }

FORWARD(HRESULT, DirectInputCreateA,
        (HINSTANCE h, DWORD v, void **pp, void *unk), (h, v, pp, unk))
FORWARD(HRESULT, DirectInputCreateW,
        (HINSTANCE h, DWORD v, void **pp, void *unk), (h, v, pp, unk))
FORWARD(HRESULT, DirectInputCreateEx,
        (HINSTANCE h, DWORD v, const void *riid, void **pp, void *unk),
        (h, v, riid, pp, unk))
FORWARD(HRESULT, DllCanUnloadNow,     (void), ())
FORWARD(HRESULT, DllGetClassObject,
        (REFCLSID rclsid, REFIID riid, LPVOID *ppv), (rclsid, riid, ppv))
FORWARD(HRESULT, DllRegisterServer,   (void), ())
FORWARD(HRESULT, DllUnregisterServer, (void), ())

/* ============================= DllMain ============================= */

BOOL WINAPI DllMain(HINSTANCE hInst, DWORD reason, LPVOID reserved)
{
    (void)reserved;

    if (reason == DLL_PROCESS_ATTACH) {
        char  exePath[MAX_PATH];
        char *slash;
        HANDLE th;

        DisableThreadLibraryCalls(hInst);

        InitializeCriticalSection(&g_lock);
        g_lockReady = 1;

        if (GetModuleFileNameA(NULL, exePath, MAX_PATH)) {
            strncpy(g_logPath, exePath, MAX_PATH - 1);
            g_logPath[MAX_PATH - 1] = 0;
            slash = strrchr(g_logPath, '\\');
            if (slash) slash[1] = 0; else g_logPath[0] = 0;
            strncat(g_logPath, "mp2cn.log", MAX_PATH - strlen(g_logPath) - 1);
        }

        { FILE *f = fopen(g_logPath, "ab"); if (f) fclose(f); }  /* 诊断期用追加, 保留多轮日志 */

        LOG("===== mp2cn 全量字幕注入版 已加载 =====\n");
        LOG("[EXE] %s\n", exePath);

        th = CreateThread(NULL, 0, init_thread, NULL, 0, NULL);
        if (th) CloseHandle(th);
        else    LOG("[ERR] CreateThread 失败\n");
    }
    else if (reason == DLL_PROCESS_DETACH) {
        log_flush();   /* 进程退出时把缓冲日志落盘 */
    }
    return TRUE;
}
