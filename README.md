# Max Payne 2 - Full Chinese Translation Patch / 马克思佩恩2 完整中文汉化补丁

**English** | [中文说明见下方](#中文说明)

---

## English

A complete fan-made Chinese translation patch for **Max Payne 2: The Fall of Max Payne** (PC, works with the Steam / retail English version). It covers **~2500 subtitles**, all **menus**, and all **HUD strings**.

This repository contains **only original work**: translation files, build tools, and the source code of the font-hooking DLL. **No game assets are included** — you must own the game and use your own `MP2_English.ras`.

### How it works (Plan B)

The game reads all strings from `MP2_English.ras`. Instead of hooking text at runtime, the build tool **writes the Chinese text directly back into the archive** using single-byte high-bit codes (one hanzi = one byte `0x80–0xFE`). Each line's hanzi are packed onto shared 128-slot font disks (`font_cn_N.tga`, rendered from a TrueType font). A small `dinput.dll` hook intercepts text rendering and swaps the active font disk per string (matched by FNV-1a hash). The result: full Chinese with the game's own text pipeline, zero text-matching hacks.

### Requirements

- Python 3.8+ with Pillow: `pip install pillow`
- A Chinese font (one of):
  - [Source Han Sans SC (思源黑体)](https://github.com/adobe-fonts/source-han-sans/releases) — SIL OFL
  - [MiSans](https://hyperos.mi.com/font) — free, allows redistribution
- A legal copy of Max Payne 2 (English version)

### Usage

Double-click `run_tool.bat` (Windows) or run `python mp2_translation_tool.py` for the interactive menu (switchable 中文/English):

```
[1] Extract text from RAS     — subtitles / menus / HUD from your MP2_English.ras
[2] Full dump                 — all .txt/.ltx files in the archive
[3] Build Chinese RAS         — apply translations, render font disks, gen subs_all.h
[4] Repack RAS                — pack an edited file tree back into the archive
[5] Verify RAS                — CRC + integrity check
[6] Install into game dir     — backup original, copy RAS + fonts + DLL
[L] Switch language / 切换语言
```

Typical player flow: run `3` (point at your game's `MP2_English.ras` + a font), then `6` (point at your game directory). The original RAS is backed up as `MP2_English.ras.bak` automatically.

### Building the DLL yourself

The prebuilt `dll_source/dinput.dll` matches the bundled translations. If you modify translations, regenerate `subs_all.h` with mode `3` and recompile:

```
zig cc -target x86-windows-gnu -shared -O2 -o dinput.dll dll_source/main.c dll_source/dinput.def -lkernel32 -luser32
```

### Steam Deck / Linux (Proton)

Proton ignores the game's local `dinput.dll` by default. Add this launch option:

```
WINEDLLOVERRIDES="dinput=n,b" %command%
```

### Contributing translations

Subtitle translations live in `translations/subs_zh/sNN_*.py` (`SUBS = { id: "中文" }`), menus and HUD in `translations/ui_zh.py` (`MENU` / `HUD` dicts). Keep placeholders like `%s`, `#USE#` intact. Keep each subtitle under ~27 hanzi (engine width limit). Terminology: see `translations/GLOSSARY.md`.

### Legal / Disclaimer

This is an **unofficial fan project**. *Max Payne* and *Max Payne 2* are trademarks of Remedy Entertainment / Rockstar Games. This repository distributes **no copyrighted game content**; the tools require the user's own legally obtained copy of the game. Provided as-is, under the MIT License (see `LICENSE`).

---

## 中文说明

《马克思佩恩2：马克思的堕落》PC 英文版的完整民间中文汉化补丁，覆盖 **约 2500 条字幕**、全部**菜单**和 **HUD 文本**。

本仓库**只包含原创内容**：译文文件、构建工具、字体钩子 DLL 源码。**不含任何游戏素材**——你需要自备正版游戏和自己的 `MP2_English.ras`。

### 原理（方案B）

游戏所有文本都从 `MP2_English.ras` 读取。构建工具把中文以**单字节高位编码**（一个汉字 = 一个 `0x80–0xFE` 字节）直接写回归档；每句的汉字装箱到共享的 128 槽字盘（`font_cn_N.tga`，由 TrueType 字体渲染）；一个小型 `dinput.dll` 钩子按字符串 FNV-1a 哈希查表、逐串切换字盘。文本走游戏自身渲染，没有任何运行时文本匹配的补丁。

### 使用方法

双击 `run_tool.bat` 或运行 `python mp2_translation_tool.py` 进入交互菜单（可切中/英文）：

1. `[3] 构建中文 RAS` —— 指向你游戏目录里的 `MP2_English.ras` + 一个中文字体文件
2. `[6] 安装补丁到游戏目录` —— 自动备份原版（`.bak`），复制新 RAS + 字盘 + DLL

想自己改译文：编辑 `translations/subs_zh/*.py` 和 `translations/ui_zh.py`，重新跑 `[3]`、`[6]`；改了译文需按上面的 zig 命令重编 DLL（或直接用 `translations` 里未改动时的预编译 DLL）。

### 字体授权

- 思源黑体（Source Han Sans）：SIL OFL，可自由使用和再分发
- MiSans：小米字体，免费商用

技术细节见 `docs/font_system_notes_cn.md`（字体系统逆向笔记，中文）。

### 免责声明

本项目为**非官方粉丝作品**。《马克思佩恩》商标归 Remedy Entertainment / Rockstar Games 所有。本仓库不分发任何受版权保护的游戏内容；工具要求使用用户自己合法获得的游戏副本。按"现状"提供，代码部分采用 MIT 许可证（见 `LICENSE`）。

---

## Credits / 致谢

- RAS archive decryption based on [ernestask/libras](https://github.com/ernestask/libras)
- RAS packer, font packing, DLL hook: original work of this project

## License / 许可证

MIT — see [LICENSE](LICENSE).
