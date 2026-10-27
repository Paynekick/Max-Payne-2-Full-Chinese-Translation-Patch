# Max Payne 2 字体系统逆向结论 —— 与 GTA 系汉化路线的对照

> 本文修正并取代前一版《马克思佩恩2_汉化可行性分析.md》中"用系统 TTF 渲染"的建议。
> 全部数据来自对本机 `E:\Max Payne 2` 的 8 个 `.ras` 归档实测解包，CRC32 全部校验通过。
> ⚠️ 本文为早期可行性分析笔记；**MP2M（`.mp2m` MOD 包）分发方式已于 2026-08-15 评估后否决**，最终采用方案以仓库 README 为准。

---

## 一、结论先行

Max Payne 2 的字体系统与 GTA3 / Vice City / San Andreas **属于同一类架构**：
外部可替换的位图字库 + 256 字形槽 + 单字节索引。

因此 **VC/SA 那套"内核汉化"（换字库 + 打补丁支持双字节）在 MP2 上原理完全成立**，
而且在数据层，MP2 比 GTA **更容易改**。

唯一比 GTA 麻烦的地方只有一处：MP2 的字库是**一维单行横条**，不能像 GTA 的
二维网格那样靠加行扩容，必须由补丁接管字形定位逻辑。

---

## 二、实测到的字体系统全貌

### 2.1 字库文件（`MP2_Data.ras` → `data/sharedtextures/`）

| 文件 | 尺寸 | 格式 | 用途 |
|---|---|---|---|
| `font_univers.tga` | 3126 × 27 | TGA 24bit | 主菜单常规字 |
| `font_univers_bright.tga` | 3126 × 27 | TGA 24bit | 主菜单选中字 |
| `font_univers_alpha.tga` | 3126 × 27 | TGA 24bit | 上二者的 alpha 遮罩 |
| `font_universal_medium.tga` | 2300 × 23 | TGA 24bit | **HUD / 物品栏 / 暂停界面** |
| `font_universal_medium_alpha.tga` | 2300 × 23 | TGA 24bit | alpha 遮罩 |
| `font_univers_verysmall.tga` | 2512 × 19 | TGA 24bit | 工具提示 |
| `font_univers_verysmall_alpha.tga` | 2512 × 19 | TGA 24bit | alpha 遮罩 |
| `font_tahoma.pcx` / `_alpha.pcx` | 988 × 14 | PCX 8bit | 控制台 |
| `font_console8pt.pcx` / `_alpha.pcx` | 832 × 11 | PCX 8bit | 控制台 |

注意：**颜色图与 alpha 图是两张独立文件**，替换字库时必须成对生成。

### 2.2 字库布局：单行横条 + 顶行标记像素

实测 `font_univers.tga` 顶行（TGA 为 bottom-left 原点，需翻转后取图像第 0 行）
只有纯白 `(255,255,255)` 与纯黑两种像素：

```
白色游程数 = 256        ← 恰好 256 个字形槽
黑色游程数 = 257        ← 槽间 1px 分隔
白色游程宽度 = 该字形的实际宽度（1 ~ 24 px，可变宽）
```

三种 TGA 字库测出的白色游程数**全部恰好为 256**，不多不少。

**即：字形宽度表不在 exe 里，也不在任何配置文件里，而是画在图片自己的顶行上。**
这是 MP2 相对 GTA 的一个重大优势——换字库不需要改任何二进制宽度表。

### 2.3 字形索引 = 字节值

按游程顺序取出第 N 个槽位并渲染为字符画，验证结果：

| 槽位 | 渲染结果 |
|---|---|
| 65 | `A` |
| 66 | `B` |
| 77 | `M` |

**字形索引与字节值严格一一对应，0x00–0xFF 共 256 槽。**

### 2.4 字库文件名是明文可配置的

字体路径直接写在纯文本配置里，不是硬编码：

```ini
# data/menu/menu.txt
NormalFont        = "..\sharedtextures\font_univers.tga";
NormalFontAlpha   = "..\sharedtextures\font_univers_alpha.tga";
SelectedFont      = "..\sharedtextures\font_univers_bright.tga";
ToolTipFont       = "..\sharedtextures\font_univers_verysmall.tga";

# data/hud/hud.txt
Font              = "..\sharedtextures\font_universal_medium.tga";
InventoryFont     = "..\sharedtextures\font_universal_medium.tga";

# data/graphicnovel/graphicnovel.txt
PauseFont         = "..\sharedtextures\font_universal_medium.tga";
ToolTipFont       = "..\sharedtextures\font_univers_verysmall.tga";

# data/console/console.txt
Filename          = "..\sharedtextures\font_tahoma.pcx";
```

**改一行文本就能让引擎去加载任意自定义字库文件。** GTA 的 `fonts.txd` 是硬编码文件名，这一点 MP2 更友好。

### 2.5 原生 MOD 格式 `.mp2m`（仅作记录，本项目未采用）

游戏目录下存在第三方 MOD 包（`.mp2m`，同为 RAS 容器格式，由官方 Mod Tools RASMaker2 生成、引擎原生加载）：

```
HellsingMod0.7Beta.mp2m    143 MB
RezzieModv32.mp2m           31 MB
```

> ⚠️ **本项目否决 MP2M 分发**：`.mp2m` 只能覆盖已有资源，无法注入根目录 `dinput.dll`、也无法让引擎从 MOD 流读取 `font_cn_N.tga` 等补丁字盘。最终可发形态为「改写 `MP2_English.ras` + 释放 `dinput.dll` + 字盘」的覆盖式补丁（详见 README），与 GTA 装 MOD 依赖 ASI Loader 的处境类似，并无原生优势。

---

## 三、与 GTA 系汉化的逐项对照

| 维度 | GTA3 / VC / SA | Max Payne 2 | 谁更容易 |
|---|---|---|---|
| 字库载体 | `fonts.txd` 贴图字典 | `font_*.tga` / `.pcx` 图片 | 平手 |
| 字形容量 | 16×16 网格 = 256 | 单行横条 = 256 | 平手 |
| 索引方式 | 单字节 | 单字节 | 平手 |
| 字形宽度表 | 需另改（exe / 表文件） | **画在图片顶行，改图即改宽度** | **MP2 胜** |
| 字库文件名 | 硬编码 | **写在 .txt 明文配置里** | **MP2 胜** |
| 文本载体 | `american.gxt`（二进制，需专用工具） | **纯文本 `.txt`，`String = "..."` 格式** | **MP2 胜** |
| MOD 加载 | 依赖社区 ASI Loader / CLEO | 官方 `.mp2m` 原生支持（但本项目否决该分发方式） | 理论 MP2 胜 |
| 扩容方向 | 网格可纵向加行 | 单行只能横向拉长，撞纹理宽度上限 | **GTA 胜** |

**净结论：MP2 在 7 项里 4 胜 3 平 1 负。数据层比 GTA 好改得多，
唯一的硬骨头（双字节 + 扩容）和 GTA 完全是同一块，而且是已被解决过的问题。**

---

## 四、为什么单行横条是硬墙

实测文本体量（尚不含 `.ldb` 关卡内实时对白）：

```
可翻译英文句子   1,727 条
英文字符总量     78,161 字符
折算中文字数     ≈ 43,000 字
估计唯一汉字数   ≈ 1,800 – 2,200 字
```

若沿用原有的单行横条布局，按每字 24px 宽计算：

```
2000 字 × 25px ≈ 50,000 px 宽
```

即便现代 GPU 的最大纹理边长（16384）也放不下，**溢出约 3 倍**；
DX8 时代硬件上限（2048 / 4096）更是差了一个数量级。

**所以不能简单"把横条拉长"，必须让补丁接管字形定位。**

---

## 五、修正后的技术方案（VC/SA 路线）

### ✗ 已否决：系统 TTF 实时渲染
即 GTA4 早期 / SA 早期那套，用 GDI / DirectWrite 在画面上叠字幕。
问题正如社区经验所示：劫持显示层，与宽屏补丁、D3D 封装、各种 DX Wrapper
互相打架，兼容性差，也是后来 GTA 汉化弃用该思路的原因。
本作根目录已有 `d3d8.dll`（WidescreenFix 封装），叠加渲染层冲突风险更高。

### ✓ 采用：离线烘焙字库 + 钩住字形查表

**Step 1 — 提取全部文本**
用已完成的 `ras_extract.py` 解出 `.txt` / `.ldb` 中的英文原文。
格式统一为 `[键名] String = "英文"`，翻译难度等同改 ini。

**Step 2 — 统计唯一汉字，生成有限字库**
对译文做唯一字符统计（预计 1800–2200 字），离线用中文 TTF
（思源黑体 / 方正兰亭）烘焙成 **2048 × 2048 网格图集**：

```
24 × 24 px 单元格 → 85 × 85 = 7,225 字形槽
```

一张贴图容量远超需求，且同时生成配套的 `_alpha` 遮罩图，
沿用引擎原有的"颜色图 + alpha 图"双文件约定。

**Step 3 — 编码重映射**
译文以双字节编码（GBK 或自定义 2 字节码）写回 `.txt`，
高字节 + 低字节共同定位到图集中的格子。

**Step 4 — ASI 补丁接管字形定位**
游戏原生支持 `.asi`（`scripts/` 下已有 `MaxPayne2.WidescreenFix.asi` 为证）。
补丁只需做三件事，**不碰渲染管线**：

1. 识别双字节序列，合并为一个字形索引；
2. 把"顶行游程查宽度"改为"按网格坐标算 UV"；
3. 字形推进宽度按等宽 24px 处理（中文本就是等宽）。

英文标点与数字继续走原逻辑，中英混排不受影响。

**Step 5 — 分发形态（覆盖式补丁，非 MP2M）**
MP2M（`.mp2m`）已于 2026-08-15 否决，原因见 §2.5。实际分发为覆盖式补丁：
将译文（单字节高位编码）写回 `MP2_English.ras` 的文本文件，释放 `dinput.dll` 钩子与
`font_cn_N.tga` 字盘到游戏目录，由 `dinput.dll` 接管字形查表与换盘。

### 方案优势
- 引擎自己的文字绘制、描边、淡入淡出、排版全部原样保留；
- 与 WidescreenFix、各类 D3D Wrapper 天然不冲突（没有额外渲染层）；
- 字库离线生成，运行期零字体解析开销；
- 以覆盖式补丁分发（`dinput.dll` + 改写 `.ras` + 字盘），运行期零字体解析开销。

---

## 六、工作量评估

| 环节 | 难度 | 说明 |
|---|---|---|
| 文本提取 | ✅ 已完成 | `ras_extract.py`，CRC 全通过 |
| 文本翻译 | 低 | 约 4.3 万中文字，纯文本编辑 |
| 字库烘焙 | 低 | Python + PIL 脚本，一次成型 |
| 编码重映射 | 低 | 脚本批处理 |
| **ASI 补丁** | **高** | **唯一真正的门槛：需逆向 MAX-FX 文字绘制函数、定位字形查表点** |
| 补丁打包 | 低 | 改写 `.ras` + 释放 dll / 字盘 |

**全部难度集中在 Step 4 一处**，且这一步在 GTA 系上已有成熟先例可参考。
这也解释了为什么民间十几年只做出了图片汉化——不是文本难，是没人啃那一处逆向。

---

## 七、附：已产出的工具与证据

- `ras_extract.py` —— RAS 归档解包器（XOR 滚动解密 + Okumura LZSS）
- `mp2_extracted/` —— `MP2_English.ras` 解出的文本
- `mp2_data_texts/` —— `MP2_Data.ras` 解出的上百个配置与文本文件
- `mp2_fonts/` —— 解出的 11 个原始字库文件（TGA / PCX）
