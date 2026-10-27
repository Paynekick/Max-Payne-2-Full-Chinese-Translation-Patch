# -*- coding: utf-8 -*-
"""
Max Payne 2 - Full Chinese Translation Patch : all-in-one command line tool
马克思佩恩2 完整中文汉化补丁 : 一体化命令行工具

Single-file tool. No game assets are included or required to run this file;
you point it at YOUR OWN copy of Max Payne 2.
单文件工具。本文件不包含、也不分发任何游戏素材；请指向你自己的正版游戏文件。

Commands (interactive menu if run without arguments):
    extract  <ras> [outdir]        Extract subtitles / menus / HUD text
    dump     <ras> [outdir]        Extract ALL .txt/.ltx files from archive
    build    <ras> [font] [outdir] Build Chinese RAS + font disks + subs_all.h
    repack   <ras> <tree> <out>    Repack an edited file tree back into a RAS
    verify   <ras>                 Verify archive CRCs and readability
    install  <game_dir> [outdir]   Install built patch into the game directory
    lang     en|zh                 Switch interface language

RAS decrypt algorithm reverse-engineered from ernestask/libras (MIT).
The packer (build_ras) is an original implementation of this project.
"""
import os
import re
import sys
import json
import struct
import zlib
import shutil

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(TOOL_DIR, "config.json")

# ----------------------------------------------------------------------------
# i18n
# ----------------------------------------------------------------------------
LANG = "zh"

STR = {
    "zh": {
        "title": "马克思佩恩2 完整中文汉化补丁 - 一体化工具",
        "menu": ("[1] 从 RAS 提取文本 (字幕/菜单/HUD)\n"
                 "[2] 全量导出 (.txt/.ltx 全部文本文件)\n"
                 "[3] 构建中文 RAS (应用译文 + 渲染字盘)\n"
                 "[4] 重打包 RAS (把修改后的文件树打回归档)\n"
                 "[5] 校验 RAS (CRC + 完整性)\n"
                 "[6] 安装补丁到游戏目录\n"
                 "[L] 切换语言 / Language\n"
                 "[Q] 退出"),
        "pick": "请选择: ",
        "bye": "再见!",
        "bad_choice": "无效选择。",
        "ask_ras": "请输入 MP2_English.ras 路径: ",
        "ask_font": "请输入中文字体文件路径 (.ttf/.otf, 例如思源黑体): ",
        "ask_out": "输出目录 [回车=默认 %s]: ",
        "ask_tree": "请输入已修改文件树的根目录: ",
        "ask_outras": "输出 .ras 路径: ",
        "ask_game": "请输入游戏目录 (含 MP2_English.ras): ",
        "ask_builddir": "构建产物目录 [回车=默认 output]: ",
        "ras_missing": "文件不存在: %s",
        "dir_missing": "目录不存在: %s",
        "not_ras": "不是有效的 RAS 归档 (magic 不对): %s",
        "extracting": "正在提取文本...",
        "extract_done": "提取完成: %d 个文件 -> %s",
        "dump_done": "全量导出完成: %d 个文件 -> %s",
        "loading_tr": "正在加载译文...",
        "tr_stats": "字幕 %d 条, 菜单 %d 条, HUD %d 条",
        "tr_missing": "!! 译文文件缺失: %s (请确认 translations/ 目录完整)",
        "packing": "装箱结果: %d 行 -> %d 张字盘",
        "dyn_chars": "动态串汉字数(强制盘0): %d",
        "building": "正在写回 .ras ...",
        "build_ok": "构建完成: %s",
        "render": "正在渲染字盘...",
        "disk": "盘%d: %d 字, 宽=%d%s",
        "disk_over": "  !! 超过 TGA 4096 宽度上限!",
        "width_warn": "  !! 字幕 %s 含 %d 个汉字 (>27, 引擎宽度上限约27, 会崩溃! 请缩短译文)",
        "rewrite_file": "改写 %s (%d -> %d 字符)",
        "rewritten": "共改写 %d 个文件",
        "verify_ok": "CRC 校验全部通过: header/file_table/dir_table",
        "verify_bad": "CRC 校验失败: header=%s file_table=%s dir_table=%s",
        "verify_files": "文件数 %d, 目录数 %d, 数据区基址 0x%X",
        "repacking": "正在重打包...",
        "repack_hit": "替换 %d 个文件, 其余 %d 个原样保留",
        "repack_miss": "!! 以下文件在归档中找不到对应条目(已跳过): %s",
        "repack_ok": "重打包完成: %s",
        "install_backup": "已备份原始 RAS -> %s",
        "install_ras": "RAS -> %s",
        "install_dll": "DLL -> %s",
        "install_fonts": "字盘 0..%d 已复制 (共 %d 张, 两处 sharedtextures 目录)",
        "install_no_build": "构建产物不存在 (%s), 请先执行 [3] 构建。",
        "install_ok": "安装完成。启动游戏即可。",
        "lang_done": "语言已切换为中文。",
        "need_pillow": "需要 Pillow: 请先执行  pip install pillow",
        "font_missing": "字体文件不存在: %s",
        "cfg_saved": "(路径已保存到 config.json, 下次回车可沿用)",
        "no_dll": "未找到 dll_source/dinput.dll, 跳过 DLL 安装。",
        "err": "出错: %s",
    },
    "en": {
        "title": "Max Payne 2 Full Chinese Translation Patch - All-in-one Tool",
        "menu": ("[1] Extract text from RAS (subtitles / menus / HUD)\n"
                 "[2] Full dump (all .txt/.ltx files in archive)\n"
                 "[3] Build Chinese RAS (apply translations + render font disks)\n"
                 "[4] Repack RAS (pack an edited file tree back)\n"
                 "[5] Verify RAS (CRC + integrity)\n"
                 "[6] Install patch into game directory\n"
                 "[L] Switch language / 切换语言\n"
                 "[Q] Quit"),
        "pick": "Choose: ",
        "bye": "Bye!",
        "bad_choice": "Invalid choice.",
        "ask_ras": "Path to MP2_English.ras: ",
        "ask_font": "Path to Chinese font file (.ttf/.otf, e.g. Source Han Sans SC): ",
        "ask_out": "Output directory [Enter=default %s]: ",
        "ask_tree": "Root directory of the edited file tree: ",
        "ask_outras": "Output .ras path: ",
        "ask_game": "Game directory (contains MP2_English.ras): ",
        "ask_builddir": "Build output directory [Enter=default 'output']: ",
        "ras_missing": "File not found: %s",
        "dir_missing": "Directory not found: %s",
        "not_ras": "Not a valid RAS archive (bad magic): %s",
        "extracting": "Extracting text...",
        "extract_done": "Extraction done: %d files -> %s",
        "dump_done": "Full dump done: %d files -> %s",
        "loading_tr": "Loading translations...",
        "tr_stats": "Subtitles %d, Menu %d, HUD %d",
        "tr_missing": "!! Missing translation file: %s (check the translations/ folder)",
        "packing": "Bin packing: %d rows -> %d font disks",
        "dyn_chars": "Dynamic-string hanzi (forced to disk 0): %d",
        "building": "Writing back .ras ...",
        "build_ok": "Build finished: %s",
        "render": "Rendering font disks...",
        "disk": "Disk%d: %d glyphs, width=%d%s",
        "disk_over": "  !! exceeds TGA 4096 width limit!",
        "width_warn": "  !! subtitle %s has %d hanzi (>27, engine width limit ~27, WILL CRASH! shorten it)",
        "rewrite_file": "Rewrote %s (%d -> %d chars)",
        "rewritten": "Rewrote %d files total",
        "verify_ok": "All CRC checks passed: header/file_table/dir_table",
        "verify_bad": "CRC check FAILED: header=%s file_table=%s dir_table=%s",
        "verify_files": "%d files, %d dirs, data base 0x%X",
        "repacking": "Repacking...",
        "repack_hit": "Replaced %d files, kept %d as-is",
        "repack_miss": "!! no matching entry in archive (skipped): %s",
        "repack_ok": "Repack finished: %s",
        "install_backup": "Original RAS backed up -> %s",
        "install_ras": "RAS -> %s",
        "install_dll": "DLL -> %s",
        "install_fonts": "Font disks 0..%d copied (%d files, into both sharedtextures dirs)",
        "install_no_build": "Build output not found (%s); run [3] Build first.",
        "install_ok": "Install complete. Launch the game.",
        "lang_done": "Language switched to English.",
        "need_pillow": "Pillow required: run  pip install pillow",
        "font_missing": "Font file not found: %s",
        "cfg_saved": "(paths saved to config.json; press Enter to reuse next time)",
        "no_dll": "dll_source/dinput.dll not found, skipping DLL install.",
        "err": "Error: %s",
    },
}


def t(key, *args):
    s = STR[LANG].get(key, key)
    return s % args if args else s


# ----------------------------------------------------------------------------
# RAS archive library (Max Payne 2 / MAX-FX .ras format)
# Decrypt algorithm reverse-engineered from ernestask/libras.
# The packer (build_ras) is an original implementation of this project.
# ----------------------------------------------------------------------------
HEADER_SIZE = 0x2C
MAGIC = b"RAS\x00"


def _rotl8(b, n):
    n &= 7
    return ((b << n) | (b >> (8 - n))) & 0xFF


def _rotr8(b, n):
    n &= 7
    return ((b >> n) | (b << (8 - n))) & 0xFF


def _next_seed(s):
    """seed evolution: s = s*0xAB - (s/0xB1)*0x763D, C truncation toward zero"""
    sb = s if s < 0x80000000 else s - 0x100000000
    q = abs(sb) // 0xB1
    if sb < 0:
        q = -q
    return (sb * 0xAB - q * 0x763D) & 0xFFFFFFFF


def decode_stream(data, seed):
    out = bytearray(len(data))
    s = seed
    for i in range(len(data)):
        s = _next_seed(s)
        x = _rotl8(data[i], i % 5)
        out[i] = ((x ^ ((i + 3) * 6)) + (s & 0xFF)) & 0xFF
    return bytes(out)


def encode_stream(data, seed):
    """exact inverse of decode_stream"""
    out = bytearray(len(data))
    s = seed
    for i in range(len(data)):
        s = _next_seed(s)
        y = (data[i] - (s & 0xFF)) & 0xFF
        y ^= ((i + 3) * 6) & 0xFF
        out[i] = _rotr8(y, i % 5)
    return bytes(out)


def lzss_decompress(blob):
    assert blob[:4] == b"RA->", blob[:4]
    ring = [0] * 4096
    rp = 18
    out = bytearray()
    s = 12
    end = len(blob)
    while s < end:
        flags = blob[s]
        s += 1
        for i in range(8):
            if s >= end:
                break
            if flags & (1 << i):
                b = blob[s]
                s += 1
                ring[rp] = b
                rp = (rp + 1) % 4096
                out.append(b)
            else:
                if s + 1 >= end:
                    break
                b0, b1 = blob[s], blob[s + 1]
                s += 2
                ptr = ((b1 & 0xF0) << 4) | b0
                ln = (b1 & 0xF) + 3
                for _ in range(ln):
                    b = ring[(ptr + 0x12 + _) % 4096]
                    ring[rp] = b
                    rp = (rp + 1) % 4096
                    out.append(b)
    return bytes(out)


class RasEntry(object):
    __slots__ = ("name", "size", "entry_size", "res0", "parent",
                 "res1", "comp", "time", "offset", "_blob", "_dirpath")


class RasArchive(object):
    def __init__(self, path):
        self.path = path
        self.fh = open(path, "rb")
        head = self.fh.read(HEADER_SIZE)
        if head[:4] != MAGIC:
            self.fh.close()
            raise ValueError("bad magic: %r" % head[:4])
        self.seed = struct.unpack_from("<i", head, 4)[0]
        hdr = bytearray(head)
        hdr[8:HEADER_SIZE] = decode_stream(bytes(head[8:HEADER_SIZE]), self.seed)
        self.plain_header = bytes(hdr)
        (self.file_count, self.dir_count, self.fts, self.dts,
         self.archive_version, self.header_crc, self.file_crc,
         self.dir_crc, self.format_version) = struct.unpack_from("<IIIIIIIII", hdr, 8)

        self.file_table = decode_stream(self.fh.read(self.fts), self.seed)
        self.dir_table = decode_stream(self.fh.read(self.dts), self.seed)
        self.data_base = HEADER_SIZE + self.fts + self.dts

        self.dirs = []
        self.dir_times = []
        p = 0
        for _ in range(self.dir_count):
            ne = self.dir_table.index(b"\x00", p)
            self.dirs.append(self.dir_table[p:ne].decode("latin-1"))
            self.dir_times.append(self.dir_table[ne + 1:ne + 17])
            p = ne + 17

        self.entries = []
        fp = 0
        off = 0
        for _ in range(self.file_count):
            ne = self.file_table.index(b"\x00", fp)
            name = self.file_table[fp:ne].decode("latin-1")
            fp = ne + 1
            size, esz, r0, par, r1, comp = struct.unpack_from("<IIIIII", self.file_table, fp)
            tm = self.file_table[fp + 24:fp + 40]
            fp += 40
            e = RasEntry()
            e.name = name
            e.size = size
            e.entry_size = esz
            e.res0 = r0
            e.parent = par
            e.res1 = r1
            e.comp = comp
            e.time = tm
            e.offset = off
            e._blob = None
            e._dirpath = self.dirs[par] if par < len(self.dirs) else "\\"
            self.entries.append(e)
            off += esz

    def full_path(self, e):
        d = e._dirpath
        return e.name if d == "\\" else d.lstrip("\\").replace("\\", "/") + "/" + e.name

    def raw(self, e):
        if e._blob is not None:
            return e._blob
        self.fh.seek(self.data_base + e.offset)
        return self.fh.read(e.entry_size)

    def content(self, e):
        b = self.raw(e)
        return lzss_decompress(b) if b[:4] == b"RA->" else b

    def verify(self):
        h = bytearray(self.plain_header)
        struct.pack_into("<I", h, 0x1C, 0)
        ok_h = (zlib.crc32(bytes(h)) & 0xFFFFFFFF) == self.header_crc
        ok_f = (zlib.crc32(self.file_table) & 0xFFFFFFFF) == self.file_crc
        ok_d = (zlib.crc32(self.dir_table) & 0xFFFFFFFF) == self.dir_crc
        return ok_h, ok_f, ok_d

    def close(self):
        self.fh.close()


def build_ras(out_path, dirs, dir_times, files, seed, archive_version, format_version):
    """
    dirs      : ["\\", "\\data", ...] full path list
    dir_times : 16-byte SYSTEMTIME list, same length as dirs
    files     : [(name, parent_index, raw_bytes, size, res0, res1, comp, time16), ...]
                raw_bytes = final data-area bytes (with RA-> header if compressed)
                size = uncompressed size (== len(raw_bytes) when uncompressed)
    """
    dt = bytearray()
    for name, tm in zip(dirs, dir_times):
        dt += name.encode("latin-1") + b"\x00" + tm
    ft = bytearray()
    for (name, parent, raw, size, r0, r1, comp, tm) in files:
        ft += name.encode("latin-1") + b"\x00"
        ft += struct.pack("<IIIIII", size, len(raw), r0, parent, r1, comp)
        ft += tm
    dt = bytes(dt)
    ft = bytes(ft)

    hdr = bytearray(HEADER_SIZE)
    hdr[0:4] = MAGIC
    struct.pack_into("<i", hdr, 4, seed)
    struct.pack_into("<IIIIIIIII", hdr, 8,
                     len(files), len(dirs), len(ft), len(dt),
                     archive_version,
                     0,  # header_crc placeholder (crc computed with field = 0)
                     zlib.crc32(ft) & 0xFFFFFFFF,
                     zlib.crc32(dt) & 0xFFFFFFFF,
                     format_version)
    hcrc = zlib.crc32(bytes(hdr)) & 0xFFFFFFFF
    struct.pack_into("<I", hdr, 0x1C, hcrc)

    with open(out_path, "wb") as o:
        o.write(hdr[:8])
        o.write(encode_stream(bytes(hdr[8:HEADER_SIZE]), seed))
        o.write(encode_stream(ft, seed))
        o.write(encode_stream(dt, seed))
        for (_n, _p, raw, _s, _r0, _r1, _c, _t) in files:
            o.write(raw)
    return out_path


# ----------------------------------------------------------------------------
# Translation data
# ----------------------------------------------------------------------------
CHAPTERS = [
    "s03_first_hospital", "s04_warehouse", "s05_first_vodka", "s06_first_dream",
    "s07_maxs_apartment", "s08_first_address_unknown", "s09_upper_east_side",
    "s10_police_station", "s11_second_address_unknown", "s12_condemned_building",
    "s13_construction_site", "s14_second_dream",
    "s15_second_hospital", "s16_second_vodka", "s17_crackhouse", "s18_gognittis_lot",
    "s19_third_address_unknown", "s20_third_dream", "s21_manor", "s22_end",
    "scinematics", "stv_series",
]


def load_translations(tr_dir):
    """Load bundled translations: translations/subs_zh/*.py + translations/ui_zh.py"""
    sub_path = os.path.join(tr_dir, "subs_zh")
    ui_path = os.path.join(tr_dir, "ui_zh.py")
    for p in (sub_path, ui_path):
        if not os.path.exists(p):
            raise FileNotFoundError(p)
    SUB = {}
    for name in CHAPTERS:
        fp = os.path.join(sub_path, name + ".py")
        if not os.path.exists(fp):
            raise FileNotFoundError(fp)
        ns = {}
        exec(open(fp, encoding="utf-8").read(), ns)
        SUB.update(ns.get("SUBS", {}))
    ui = {}
    exec(open(ui_path, encoding="utf-8").read(), ui)
    return SUB, ui["MENU"], ui["HUD"]


def is_wide(ch):
    """characters occupying a font-disk slot: anything above ASCII"""
    return ord(ch) > 0x7F


# ----------------------------------------------------------------------------
# [1] / [2] Extraction
# ----------------------------------------------------------------------------
SUBDIR_PREFIX = "data/database/subtitles/"
STRINGDEFINES = "data/database/stringdefines.h"
STRINGTABLE = "data/database/stringtable.txt"


def _check_ras(path):
    if not os.path.isfile(path):
        print(t("ras_missing", path))
        return None
    try:
        a = RasArchive(path)
    except Exception as ex:
        print(t("not_ras", path), ex)
        return None
    return a


def _write_tree(outdir, relpath, data):
    dst = os.path.join(outdir, relpath.replace("/", os.sep))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as f:
        f.write(data)


def cmd_extract(ras, outdir=None):
    outdir = outdir or os.path.join(TOOL_DIR, "extracted")
    a = _check_ras(ras)
    if not a:
        return
    print(t("extracting"))
    n = 0
    try:
        for e in a.entries:
            p = a.full_path(e).replace("//", "/").lower()
            if p.startswith(SUBDIR_PREFIX) and p.endswith(".h") \
               or p in (STRINGDEFINES, STRINGTABLE):
                _write_tree(outdir, p, a.content(e))
                n += 1
    finally:
        a.close()
    print(t("extract_done", n, outdir))


def cmd_dump(ras, outdir=None):
    outdir = outdir or os.path.join(TOOL_DIR, "extracted_full")
    a = _check_ras(ras)
    if not a:
        return
    n = 0
    try:
        for e in a.entries:
            if not e.name.lower().endswith((".txt", ".ltx")):
                continue
            try:
                content = a.content(e)
            except Exception:
                continue
            if len(content) < 2_000_000:
                _write_tree(outdir, a.full_path(e).replace("//", "/").lower(), content)
                n += 1
    finally:
        a.close()
    print(t("dump_done", n, outdir))


# ----------------------------------------------------------------------------
# [3] Build Chinese RAS  (Plan B: high-byte single-codeunit Chinese written
#     back into the RAS; the DLL only swaps font disks, never replaces text)
# ----------------------------------------------------------------------------
CH, FS, IMG_H, HAN_W = 20, 16, 22, 20
OUTLINE = 2  # black outline width in px (glyph + outline must fit the 20px cell)
SLOTS = 128  # slots per disk: high area 0x80-0xFF
MAX_SUBTITLE_HANZI = 27  # engine width check: ~380px / 13.8px per hanzi

dyn_re = re.compile(r'#\w+#|%[0-9.]*[sdif]')


def fnv1a_rtrim(s):
    b = s.encode("latin-1", "replace")
    while b and (b[-1] in (0x20, 0x09)):
        b = b[:-1]
    h = 2166136261
    for x in b:
        h ^= x
        h = (h * 16777619) & 0xFFFFFFFF
    return h if h != 0 else 1


PAT_SUB = re.compile(r'(\[([^\]]+)\]\s*String\s*=\s*")((?:[^"\\]|\\.)*)(")')
PAT_DEF = re.compile(r'(#define\s+(\w+)\s+")((?:[^"\\]|\\.)*)(")')
PAT_HUD = re.compile(r'(\[(\w+)\]\s*String\s*=\s*")((?:[^"\\]|\\.)*)(")')


def _save_tga(im, path):
    w, h = im.size
    px = im.load()
    hdr = bytearray(18)
    hdr[2] = 2
    struct.pack_into("<HHHH", hdr, 8, 0, 0, w, h)
    hdr[16] = 24
    body = bytearray()
    for y in range(h - 1, -1, -1):
        for xx in range(w):
            r, g, b = px[xx, y]
            body += bytes((b, g, r))
    with open(path, "wb") as f:
        f.write(bytes(hdr) + bytes(body))


def build_disk(chars128, base):
    """Render one font disk: main (white glyph + black outline) + alpha TGA."""
    from PIL import Image, ImageDraw, ImageFont
    HAN = list(chars128)
    while len(HAN) < SLOTS:
        HAN.append("口")
    HAN = HAN[:SLOTS]
    fh = ImageFont.truetype(FONT_PATH, FS)
    fa = ImageFont.truetype(FONT_PATH, FS)
    asc, desc = fh.getmetrics()
    baseline = 1 + asc + max(0, (CH - (asc + desc)) // 2)
    text_y = baseline - asc
    if text_y < 1:
        text_y = 1
    widths = []
    glyphs = []
    probe = Image.new("L", (64, 64))
    pd = ImageDraw.Draw(probe)
    for code in range(256):
        if code < 32 or code == 127:
            widths.append(1)
            glyphs.append(None)
        elif code == 32:
            widths.append(6)
            glyphs.append(None)
        elif code < 127:
            ch = chr(code)
            w = max(2, int(round(pd.textlength(ch, font=fa))))
            widths.append(w)
            glyphs.append((ch, fa))
        else:
            widths.append(HAN_W)
            glyphs.append((HAN[code - 128], fh))
    xs = []
    x = 2
    for w in widths:
        xs.append(x)
        x += w + 1
    total_w = x + 1
    if total_w % 2:
        total_w += 1
    main = Image.new("RGB", (total_w, IMG_H), (0, 0, 0))
    alph = Image.new("RGB", (total_w, IMG_H), (0, 0, 0))
    dm = ImageDraw.Draw(main)
    da = ImageDraw.Draw(alph)
    dm.rectangle([0, 1, total_w - 1, IMG_H - 1], fill=(255, 255, 255))
    for x0, w in zip(xs, widths):
        dm.rectangle([x0, 0, x0 + w - 1, 0], fill=(255, 255, 255))
        da.rectangle([x0, 0, x0 + w - 1, 0], fill=(255, 255, 255))
    for x0, w, g in zip(xs, widths, glyphs):
        if not g:
            continue
        ch, font = g
        bb = font.getbbox(ch)
        gw = bb[2] - bb[0]
        ox = x0 + (w - gw) // 2 - bb[0]
        oy = 1 + CH // 2 - (bb[1] + bb[3]) // 2
        if OUTLINE > 0:
            # main: black outline first, then white body on top -> black ring + white glyph
            dm.text((ox, oy), ch, font=font, fill=(0, 0, 0),
                    stroke_width=OUTLINE, stroke_fill=(0, 0, 0))
            dm.text((ox, oy), ch, font=font, fill=(255, 255, 255))
            da.text((ox, oy), ch, font=font, fill=(255, 255, 255),
                    stroke_width=OUTLINE, stroke_fill=(255, 255, 255))
        else:
            da.text((ox, oy), ch, font=font, fill=(255, 255, 255))
    da.rectangle([0, IMG_H - 1, total_w - 1, IMG_H - 1], fill=(0, 0, 0))
    _save_tga(main, base + ".tga")
    _save_tga(alph, base + "_alpha.tga")
    return total_w


FONT_PATH = None  # set by cmd_build


def cmd_build(ras, font=None, outdir=None):
    global FONT_PATH
    outdir = outdir or os.path.join(TOOL_DIR, "output")
    os.makedirs(outdir, exist_ok=True)
    tr_dir = os.path.join(TOOL_DIR, "translations")

    # --- translations ---
    print(t("loading_tr"))
    try:
        SUB, MENU, HUD = load_translations(tr_dir)
    except FileNotFoundError as ex:
        print(t("tr_missing", ex))
        return
    print(t("tr_stats", len(SUB), len(MENU), len(HUD)))

    # --- font ---
    FONT_PATH = font or CFG.get("font") or ""
    if not FONT_PATH or not os.path.isfile(FONT_PATH):
        FONT_PATH = input(t("ask_font")).strip().strip('"')
        if not FONT_PATH or not os.path.isfile(FONT_PATH):
            print(t("font_missing", FONT_PATH))
            return
    CFG["font"] = FONT_PATH
    save_cfg()
    try:
        import PIL  # noqa: F401
    except ImportError:
        print(t("need_pillow"))
        return

    # --- engine width check (informational) ---
    for k, v in SUB.items():
        n = sum(1 for c in v if is_wide(c))
        if n > MAX_SUBTITLE_HANZI:
            print(t("width_warn", k, n))

    a = _check_ras(ras)
    if not a:
        return

    # --- bin packing: one subtitle/menu/hud row must live on a single disk ---
    rows = []
    for k, v in SUB.items():
        if v.strip():
            rows.append(("sub", k, v))
    for k, v in MENU.items():
        rows.append(("menu", k, v))
    for k, v in HUD.items():
        rows.append(("hud", k, v))

    dyn_chars = set()
    for v in list(SUB.values()) + list(MENU.values()) + list(HUD.values()):
        if dyn_re.search(v):
            dyn_chars |= {c for c in v if is_wide(c)}
    print(t("dyn_chars", len(dyn_chars)))

    static_clusters = []
    for tag, k, v in rows:
        if dyn_re.search(v):
            continue
        cl = frozenset(c for c in v if is_wide(c))
        if cl:
            static_clusters.append(cl)

    bins = [set(dyn_chars)]
    for cl in sorted(static_clusters, key=len, reverse=True):
        best, best_add = -1, None
        for i, b in enumerate(bins):
            add = len(cl - b)
            if len(b) + add <= SLOTS and (best_add is None or add < best_add):
                best, best_add = i, add
                if add == 0:
                    break
        if best < 0:
            bins.append(set(cl))
        else:
            bins[best] |= cl

    D = len(bins)
    print(t("packing", len(rows), D))
    disk_chars = [sorted(b) for b in bins]
    disk_map = [{c: i for i, c in enumerate(chars)} for chars in disk_chars]
    assert all(len(b) <= SLOTS for b in bins), "bin overflow"
    assert not (dyn_chars - set(disk_chars[0])), "dynamic hanzi not all on disk 0"

    def encode(line, did):
        out = []
        for ch in line:
            o = ord(ch)
            if o < 0x80:
                out.append(ch)
            else:
                out.append(chr(0x80 + disk_map[did][ch]))
        return "".join(out)

    row_disk = {}
    row_enc = {}
    for tag, k, v in rows:
        cl = {c for c in v if is_wide(c)}
        did = 0
        if cl and not cl <= set(disk_chars[0]):
            did = next(i for i, b in enumerate(bins) if cl <= b)
        row_disk[(tag, k)] = did
        row_enc[(tag, k)] = encode(v, did)

    # --- patch text files ---
    print(t("building"))

    def patch_sub(text):
        hits = []

        def rep(m):
            sid = m.group(2)
            if sid in SUB and SUB[sid].strip():
                enc = row_enc[("sub", sid)]
                hits.append(sid)
                return m.group(1) + enc + m.group(4)
            return m.group(0)
        return PAT_SUB.sub(rep, text), hits

    def patch_def(text):
        def rep(m):
            key = m.group(2)
            if key in MENU:
                return m.group(1) + row_enc[("menu", key)] + m.group(4)
            return m.group(0)
        return PAT_DEF.sub(rep, text)

    def patch_hud(text):
        def rep(m):
            key = m.group(2)
            if key in HUD:
                return m.group(1) + row_enc[("hud", key)] + m.group(4)
            return m.group(0)
        return PAT_HUD.sub(rep, text)

    repl = {}
    sub_hits = 0
    try:
        for e in a.entries:
            p = a.full_path(e).replace("//", "/").lower()
            if p.startswith(SUBDIR_PREFIX) and p.endswith(".h"):
                txt, hits = patch_sub(a.content(e).decode("latin-1"))
                repl[p] = txt
                sub_hits += len(hits)
            elif p == STRINGDEFINES:
                repl[p] = patch_def(a.content(e).decode("latin-1"))
            elif p == STRINGTABLE:
                repl[p] = patch_hud(a.content(e).decode("latin-1"))
    finally:
        a.close()
    print(t("rewritten", len(repl)), "subtitles:", sub_hits)

    # --- rebuild archive ---
    a = _check_ras(ras)
    if not a:
        return
    files = []
    try:
        for e in a.entries:
            p = a.full_path(e).replace("//", "/").lower()
            if p in repl:
                data = repl[p].encode("latin-1")
                files.append((e.name, e.parent, data, len(data),
                              e.res0, e.res1, e.comp, e.time))
            else:
                files.append((e.name, e.parent, a.raw(e), e.size,
                              e.res0, e.res1, e.comp, e.time))
        a.close()
    except Exception:
        a.close()
        raise
    out_ras = os.path.join(outdir, "MP2_English_CN.ras")
    build_ras(out_ras, a.dirs, a.dir_times, files, a.seed,
              a.archive_version, a.format_version)
    print(t("build_ok", out_ras))

    # --- render font disks ---
    print(t("render"))
    # remove stale disks first (disk count may change; stale orphan disks break
    # the "build count == DLL count == deployed count" invariant)
    import glob as _g
    for f in _g.glob(os.path.join(outdir, "font_cn_*.tga")):
        try:
            os.remove(f)
        except OSError:
            pass
    over = ""
    for d in range(D):
        base = os.path.join(outdir, "font_cn_%d" % d)
        w = build_disk(disk_chars[d], base)
        flag = ""
        if w > 4096:
            flag = t("disk_over")
            over = flag
        print(t("disk", d, len(disk_chars[d]), w, flag))

    # --- subs_all.h (hash -> disk table used by the DLL) ---
    lines_h = []
    lines_h.append("/* auto-generated by mp2_translation_tool.py: high-byte string -> disk */")
    lines_h.append("#ifndef SUBS_ALL_H")
    lines_h.append("#define SUBS_ALL_H")
    lines_h.append("typedef struct { unsigned int h; int disk; } AllSub;")
    lines_h.append("static const AllSub ALL_SUBS[] = {")
    for tag, k, v in rows:
        h = fnv1a_rtrim(row_enc[(tag, k)])
        lines_h.append("  {0x%08X, %d}, /* %s:%s */" % (h, row_disk[(tag, k)], tag, k))
    lines_h.append("  {0, 0}")
    lines_h.append("};")
    lines_h.append("#define ALL_NDISKS %d" % D)
    lines_h.append("#endif")
    with open(os.path.join(outdir, "subs_all.h"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines_h) + "\n")
    if over:
        print(over)


# ----------------------------------------------------------------------------
# [4] Repack edited tree
# ----------------------------------------------------------------------------
def cmd_repack(ras, tree, out_ras):
    a = _check_ras(ras)
    if not a:
        return
    if not os.path.isdir(tree):
        print(t("dir_missing", tree))
        a.close()
        return
    print(t("repacking"))
    # index edited files by lowercase relpath (forward slashes)
    edited = {}
    for root, _dirs, fnames in os.walk(tree):
        for fn in fnames:
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, tree).replace(os.sep, "/").lower()
            edited[rel] = full
    files = []
    hit = 0
    arch_paths = set()
    try:
        for e in a.entries:
            p = a.full_path(e).replace("//", "/").lower()
            arch_paths.add(p)
            if p in edited:
                data = open(edited[p], "rb").read()
                files.append((e.name, e.parent, data, len(data),
                              e.res0, e.res1, e.comp, e.time))
                hit += 1
            else:
                files.append((e.name, e.parent, a.raw(e), e.size,
                              e.res0, e.res1, e.comp, e.time))
    finally:
        a.close()
    miss = sorted(set(edited) - arch_paths)
    if miss:
        print(t("repack_miss", ", ".join(miss[:10]) + ("..." if len(miss) > 10 else "")))
    build_ras(out_ras, a.dirs, a.dir_times, files, a.seed,
              a.archive_version, a.format_version)
    print(t("repack_hit", hit, len(files) - hit))
    print(t("repack_ok", out_ras))


# ----------------------------------------------------------------------------
# [5] Verify
# ----------------------------------------------------------------------------
def cmd_verify(ras):
    a = _check_ras(ras)
    if not a:
        return
    ok_h, ok_f, ok_d = a.verify()
    if ok_h and ok_f and ok_d:
        print(t("verify_ok"))
    else:
        print(t("verify_bad", ok_h, ok_f, ok_d))
    print(t("verify_files", a.file_count, a.dir_count, a.data_base))
    a.close()


# ----------------------------------------------------------------------------
# [6] Install
# ----------------------------------------------------------------------------
def cmd_install(game_dir, outdir=None):
    outdir = outdir or os.path.join(TOOL_DIR, "output")
    if not os.path.isdir(game_dir):
        print(t("dir_missing", game_dir))
        return
    out_ras = os.path.join(outdir, "MP2_English_CN.ras")
    if not os.path.isfile(out_ras):
        print(t("install_no_build", out_ras))
        return

    # 1) backup + replace RAS
    dst_ras = os.path.join(game_dir, "MP2_English.ras")
    bak = dst_ras + ".bak"
    if os.path.isfile(dst_ras) and not os.path.isfile(bak):
        shutil.copyfile(dst_ras, bak)
        print(t("install_backup", bak))
    shutil.copyfile(out_ras, dst_ras)
    print(t("install_ras", dst_ras))

    # 2) font disks -> both sharedtextures locations (clean stale disks first:
    #    stale orphan disks break the build/DLL/deploy disk-count invariant)
    import glob as _g
    disks = sorted(_g.glob(os.path.join(outdir, "font_cn_*.tga")))
    dsts = [os.path.join(game_dir, "sharedtextures"),
            os.path.join(game_dir, "data", "sharedtextures")]
    for d in dsts:
        if os.path.isdir(d):
            for f in _g.glob(os.path.join(d, "font_cn_*.tga")):
                try:
                    os.remove(f)
                except OSError:
                    pass
    n_copy = 0
    for d in dsts:
        os.makedirs(d, exist_ok=True)
        for f in disks:
            shutil.copyfile(f, os.path.join(d, os.path.basename(f)))
            n_copy += 1
    print(t("install_fonts", len(disks) // 2 - 1, n_copy))

    # 3) DLL (optional; prebuilt included in repo)
    dll = os.path.join(TOOL_DIR, "dll_source", "dinput.dll")
    if os.path.isfile(dll):
        dst_dll = os.path.join(game_dir, "dinput.dll")
        shutil.copyfile(dll, dst_dll)
        print(t("install_dll", dst_dll))
    else:
        print(t("no_dll"))
    print(t("install_ok"))


# ----------------------------------------------------------------------------
# Config + CLI
# ----------------------------------------------------------------------------
def load_cfg():
    if os.path.exists(CONFIG_PATH):
        try:
            return json.load(open(CONFIG_PATH, encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cfg():
    try:
        json.dump(CFG, open(CONFIG_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    except Exception:
        pass


CFG = load_cfg()


def _ask(prompt_key, default=""):
    val = input(t(prompt_key) % default if "%s" in t(prompt_key) else t(prompt_key)).strip().strip('"')
    return val or default


def _ask_plain(prompt_key):
    return input(t(prompt_key)).strip().strip('"')


def menu():
    while True:
        print("\n" + "=" * 60)
        print(t("title"))
        print("=" * 60)
        print(t("menu"))
        c = input(t("pick")).strip().lower()
        try:
            if c == "1":
                p = _ask_plain("ask_ras") or CFG.get("ras", "")
                if p:
                    CFG["ras"] = p
                    save_cfg()
                    cmd_extract(p, _ask("ask_out", os.path.join(TOOL_DIR, "extracted")))
            elif c == "2":
                p = _ask_plain("ask_ras") or CFG.get("ras", "")
                if p:
                    CFG["ras"] = p
                    save_cfg()
                    cmd_dump(p, _ask("ask_out", os.path.join(TOOL_DIR, "extracted_full")))
            elif c == "3":
                p = _ask_plain("ask_ras") or CFG.get("ras", "")
                if p:
                    CFG["ras"] = p
                    save_cfg()
                    cmd_build(p, None, _ask("ask_builddir", os.path.join(TOOL_DIR, "output")))
            elif c == "4":
                p = _ask_plain("ask_ras") or CFG.get("ras", "")
                tr = _ask_plain("ask_tree")
                ou = _ask_plain("ask_outras")
                if p and tr and ou:
                    CFG["ras"] = p
                    save_cfg()
                    cmd_repack(p, tr, ou)
            elif c == "5":
                p = _ask_plain("ask_ras") or CFG.get("ras", "")
                if p:
                    CFG["ras"] = p
                    save_cfg()
                    cmd_verify(p)
            elif c == "6":
                g = _ask_plain("ask_game") or CFG.get("game", "")
                if g:
                    CFG["game"] = g
                    save_cfg()
                    cmd_install(g, _ask("ask_builddir", os.path.join(TOOL_DIR, "output")))
            elif c == "l":
                global LANG
                LANG = "en" if LANG == "zh" else "zh"
                print(t("lang_done"))
            elif c == "q":
                print(t("bye"))
                return
            else:
                print(t("bad_choice"))
        except Exception as ex:
            print(t("err", ex))
            if LANG == "zh":
                import traceback
                traceback.print_exc()


def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    cmd = args[0].lower()
    if cmd == "lang":
        global LANG
        LANG = args[1] if len(args) > 1 and args[1] in ("en", "zh") else ("en" if LANG == "zh" else "zh")
        print(t("lang_done"))
    elif cmd == "extract":
        cmd_extract(args[1], args[2] if len(args) > 2 else None)
    elif cmd == "dump":
        cmd_dump(args[1], args[2] if len(args) > 2 else None)
    elif cmd == "build":
        cmd_build(args[1],
                  args[2] if len(args) > 2 else None,
                  args[3] if len(args) > 3 else None)
    elif cmd == "repack":
        cmd_repack(args[1], args[2], args[3])
    elif cmd == "verify":
        cmd_verify(args[1])
    elif cmd == "install":
        cmd_install(args[1], args[2] if len(args) > 2 else None)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
