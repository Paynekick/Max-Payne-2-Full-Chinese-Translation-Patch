# -*- coding: utf-8 -*-
"""
MP2 界面中文化翻译表（方案B：写回 .ras 文本，DLL 只换盘）
MENU : 对应 data/database/stringdefines.h 的 #define GCID_* "..."
HUD  : 对应 data/database/stringtable.txt 的 [KEY] String = "..."

约定：
  - 仅替换引号内的显示文本，#define / [KEY] 键名与格式保留
  - 占位符 (#USE# #PAUSE# #DODGEMODIFIER# #JUMP# #SLOWMOTION# #PAINKILLER# %s #TOTALTIME#)
    必须原样保留（游戏运行时替换为键名/数值）
  - 英文标点一律转为中文标点更适合 UI 观感，但占位符前后空格保留
"""

MENU = {
    # 英文: <unassigned>
    "GCID_UNASSIGNED": "未分配",
    # 英文: or
    "GCID_SEPARATOR": " 或 ",
    # 英文: Resume Game
    "GCID_RESUMEGAME": "继续游戏",
    # 英文: Continue the latest game you were playing
    "GCID_RESUMEGAME_TIP": "继续你最近进行中的游戏",
    # 英文: New Game
    "GCID_NEWGAME": "新游戏",
    # 英文: Start a new game from the beginning
    "GCID_NEWGAME_TIP": "从头开始一局新游戏",
    # 英文: SELECT GAME MODE
    "GCID_SELECTLEVEL": "选择游戏模式",
    # 英文: Detective
    "GCID_NORMAL": "侦探",
    # 英文: Play - the other game modes will become available when you beat Detective skill
    "GCID_NORMAL_TIP": "进行游戏——通关此难度后将解锁其它模式",
    # 英文: Hard-Boiled
    "GCID_NIGHTMARE": "铁血",
    # 英文: Step up and meet the next challenge - Beat this mode to advance to Dead on Arrival
    "GCID_NIGHTMARE_TIP": "迎接更高挑战——通关此模式解锁“到院即死”",
    # 英文: Dead on Arrival
    "GCID_HELL": "到院即死",
    # 英文: The Ultimate Test
    "GCID_HELL_TIP": "终极试炼",
    # 英文: New York Minute
    "GCID_TIMEDMODE": "纽约分钟",
    # 英文: The pressure is on as you blast your way through levels as fast as possible
    "GCID_TIMEDMODE_TIP": "争分夺秒，以最快速度杀出重围",
    # 英文: Jump to Chapter
    "GCID_LEVELSELECTOR": "跳至章节",
    # 英文: Lets you select any level you wish to play
    "GCID_LEVELSELECTOR_TIP": "可选择任意关卡进行游戏",
    # 英文: SELECT A LEVEL
    "GCID_LEVELSELECTOR_HEADLINE": "选择关卡",
    # 英文: How to Play
    "GCID_HELPSCREEN": "操作指南",
    # 英文: See the help screen to learn about the basic gameplay mechanics
    "GCID_HELPSCREEN_TIP": "查看帮助了解基本操作机制",
    # 英文: Load
    "GCID_LOAD": "读取",
    # 英文: Show a list of previously saved games
    "GCID_LOAD_TIP": "显示已保存的游戏列表",
    # 英文: LOAD GAME
    "GCID_LOADGAME": "载入游戏",
    # 英文: <empty>
    "GCID_EMPTY_LOAD": "空",
    # 英文: Load this saved game
    "GCID_EMPTY_LOAD_TIP": "载入此存档",
    # 英文: Save
    "GCID_SAVE": "保存",
    # 英文: Show a list of available save game slots
    "GCID_SAVE_TIP": "显示可用的存档槽",
    # 英文: SAVE GAME
    "GCID_SAVEGAME": "保存游戏",
    # 英文: <empty>
    "GCID_EMPTY_SAVE": "空",
    # 英文: Store your current game here
    "GCID_EMPTY_SAVE_TIP": "在此保存当前游戏",
    # 英文: Previously
    "GCID_PREVIOUSLY": "前情提要",
    # 英文: Previously on Max Payne
    "GCID_PREVIOUSLY_TIP": "马克思·佩恩前情提要",
    # 英文: Options
    "GCID_OPTIONS": "选项",
    # 英文: Modify or view controls and general gameplay, video and audio options
    "GCID_OPTIONS_TIP": "修改或查看操作、游戏、画面与音频设置",
    # 英文: Quit
    "GCID_QUIT": "退出",
    # 英文: Quit playing Max Payne
    "GCID_QUIT_TIP": "退出马克思·佩恩",
    # 英文: Credits
    "GCID_CREDITS": "制作人员",
    # 英文: View Credits
    "GCID_CREDITS_TIP": "查看制作人员",
    # 英文: OPTIONS
    "GCID_OPTIONSU": "选项",
    # 英文: Controls
    "GCID_CONTROLS": "操作控制",
    # 英文: Modify or view the movement, combat and mouse controls
    "GCID_CONTROLS_TIP": "修改或查看移动、战斗与鼠标操作",
    # 英文: CONTROLS
    "GCID_CONTROLSU": "操作控制",
    # 英文: Movement
    "GCID_MOVEMENT": "移动",
    # 英文: Modify or view the general movement controls
    "GCID_MOVEMENT_TIP": "修改或查看基础移动操作",
    # 英文: MOVEMENT KEYS
    "GCID_CHANGEMOVEMENT": "移动按键",
    # 英文: Forward -
    "GCID_FORWARD": "前进 -",
    # 英文: Press Delete to clear / Select to change the Forward movement key or button
    "GCID_FORWARD_TIP": "按 Delete 清除 / 选择以更改前进键或按键",
    # 英文: Press the new primary or alternative Forward movement key or button / ESC to cancel
    "GCID_FORWARD_CHANGE_TIP": "按下新的主用或备用前进键 / 按 ESC 取消",
    # 英文: Backward -
    "GCID_BACKWARD": "后退 -",
    # 英文: Press Delete to clear / Select to change the Backward movement key or button
    "GCID_BACKWARD_TIP": "按 Delete 清除 / 选择以更改后退键或按键",
    # 英文: Press the new primary or alternative Backward movement key or button / ESC to cancel
    "GCID_BACKWARD_CHANGE_TIP": "按下新的主用或备用后退键 / 按 ESC 取消",
    # 英文: Strafe Left -
    "GCID_STRAFELEFT": "左平移 -",
    # 英文: Press Delete to clear / Select to change the Strafe Left movement key or button
    "GCID_STRAFELEFT_TIP": "按 Delete 清除 / 选择以更改左平移键或按键",
    # 英文: Press the new primary or alternative Strafe Left movement key or button / ESC to cancel
    "GCID_STRAFELEFT_CHANGE_TIP": "按下新的主用或备用左平移键 / 按 ESC 取消",
    # 英文: Strafe Right -
    "GCID_STRAFERIGHT": "右平移 -",
    # 英文: Press Delete to clear / Select to change the Strafe Right movement key or button
    "GCID_STRAFERIGHT_TIP": "按 Delete 清除 / 选择以更改右平移键或按键",
    # 英文: Press the new primary or alternative Strafe Right movement key or button / ESC to cancel
    "GCID_STRAFERIGHT_CHANGE_TIP": "按下新的主用或备用右平移键 / 按 ESC 取消",
    # 英文: Crouch -
    "GCID_CROUCH": "蹲下 -",
    # 英文: Press Delete to clear / Select to change the Crouch key or button
    "GCID_CROUCH_TIP": "按 Delete 清除 / 选择以更改蹲下键或按键",
    # 英文: Press the new primary or alternative Crouch key or button / ESC to cancel
    "GCID_CROUCH_CHANGE_TIP": "按下新的主用或备用蹲下键 / 按 ESC 取消",
    # 英文: Jump -
    "GCID_JUMP": "跳跃 -",
    # 英文: Press Delete to clear / Select to change the Jump key or button
    "GCID_JUMP_TIP": "按 Delete 清除 / 选择以更改跳跃键或按键",
    # 英文: Press the new primary or alternative Jump key or button / ESC to cancel
    "GCID_JUMP_CHANGE_TIP": "按下新的主用或备用跳跃键 / 按 ESC 取消",
    # 英文: Use / Sniper Zoom -
    "GCID_ACTIVATE": "使用 / 狙击缩放 -",
    # 英文: Press Delete to clear / Select to change the Use / Sniper Zoom key or button
    "GCID_ACTIVATE_TIP": "按 Delete 清除 / 选择以更改使用 / 狙击缩放键或按键",
    # 英文: Press the new primary or alternative Use / Sniper Zoom key or button / ESC to cancel
    "GCID_ACTIVATE_CHANGE_TIP": "按下新的主用或备用使用 / 狙击缩放键 / 按 ESC 取消",
    # 英文: Use Painkiller -
    "GCID_USEPAINKILLER": "使用止痛药 -",
    # 英文: Press Delete to clear / Select to change the Use Painkiller key or button
    "GCID_USEPAINKILLER_TIP": "按 Delete 清除 / 选择以更改使用止痛药键或按键",
    # 英文: Press the new primary or alternative Use Painkiller key or button / ESC to cancel
    "GCID_USEPAINKILLER_CHANGE_TIP": "按下新的主用或备用使用止痛药键 / 按 ESC 取消",
    # 英文: Bullet Time Combo -
    "GCID_BULLETTIME": "子弹时间连击 -",
    # 英文: Press Delete to clear / Select to change the Bullet Time Combo key or button
    "GCID_BULLETTIME_TIP": "按 Delete 清除 / 选择以更改子弹时间连击键或按键",
    # 英文: Press the new primary or alternative Bullet Time Combo key or button / ESC to cancel
    "GCID_BULLETTIME_CHANGE_TIP": "按下新的主用或备用子弹时间连击键 / 按 ESC 取消",
    # 英文: Bullet Time only -
    "GCID_SLOWMOTION": "仅子弹时间 -",
    # 英文: Press Delete to clear / Select to change the Bullet Time only key or button (no Shootdodge)
    "GCID_SLOWMOTION_TIP": "按 Delete 清除 / 选择以更改仅子弹时间键或按键（不含翻滚闪避）",
    # 英文: Press the new primary or alternative Bullet Time only key or button (no Shootdodge) / ESC to cancel
    "GCID_SLOWMOTION_CHANGE_TIP": "按下新的主用或备用仅子弹时间键 / 按 ESC 取消",
    # 英文: Shootdodge only -
    "GCID_DODGEMODIFIER": "仅翻滚闪避 -",
    # 英文: Press Delete to clear / Select to change the Shootdodge key or button (no Bullet Time Toggle)
    "GCID_DODGEMODIFIER_TIP": "按 Delete 清除 / 选择以更改翻滚闪避键或按键（不含子弹时间）",
    # 英文: Press the new primary or alternative Shootdodge key or button (no Bullet Time Toggle) / ESC to cancel
    "GCID_DODGEMODIFIER_CHANGE_TIP": "按下新的主用或备用翻滚闪避键 / 按 ESC 取消",
    # 英文: Pause Game -
    "GCID_PAUSEGAME": "暂停游戏 -",
    # 英文: Press Delete to clear / Select to change the Pause Game key or button
    "GCID_PAUSEGAME_TIP": "按 Delete 清除 / 选择以更改暂停游戏键或按键",
    # 英文: Press the new primary or alternative Pause Game key or button / ESC to cancel
    "GCID_PAUSEGAME_CHANGE_TIP": "按下新的主用或备用暂停游戏键 / 按 ESC 取消",
    # 英文: Combat
    "GCID_COMBAT": "战斗",
    # 英文: Modify or view the combat controls
    "GCID_COMBAT_TIP": "修改或查看战斗操作",
    # 英文: COMBAT KEYS
    "GCID_CHANGECOMBAT": "战斗按键",
    # 英文: Shoot -
    "GCID_SHOOT": "射击 -",
    # 英文: Press Delete to clear / Select to change the Shoot key or button
    "GCID_SHOOT_TIP": "按 Delete 清除 / 选择以更改射击键或按键",
    # 英文: Press the new primary or alternative Shoot key or button / ESC to cancel
    "GCID_SHOOT_CHANGE_TIP": "按下新的主用或备用射击键 / 按 ESC 取消",
    # 英文: Secondary Attack -
    "GCID_ATTACK": "副攻击 -",
    # 英文: Press Delete to clear / Select to change the Secondary Attack (hit/throw) key or button
    "GCID_ATTACK_TIP": "按 Delete 清除 / 选择以更改副攻击（击打 / 投掷）键或按键",
    # 英文: Press the new primary or alternative Secondary Attack key or button / ESC to cancel
    "GCID_ATTACK_CHANGE_TIP": "按下新的主用或备用副攻击键 / 按 ESC 取消",
    # 英文: Reload -
    "GCID_RELOAD": "装弹 -",
    # 英文: Press Delete to clear / Select to change the Reload key or button
    "GCID_RELOAD_TIP": "按 Delete 清除 / 选择以更改装弹键或按键",
    # 英文: Press the new primary or alternative Reload key or button / ESC to cancel
    "GCID_RELOAD_CHANGE_TIP": "按下新的主用或备用装弹键 / 按 ESC 取消",
    # 英文: Next Weapon -
    "GCID_NEXTWEAPON": "下一武器 -",
    # 英文: Press Delete to clear / Select to change the Next Weapon selection to another key, button or to the MouseWheel
    "GCID_NEXTWEAPON_TIP": "按 Delete 清除 / 选择以更改切换下一武器键或按键",
    # 英文: Press the new primary or alternative Next Weapon selection key, button or turn the MouseWheel / ESC to cancel
    "GCID_NEXTWEAPON_CHANGE_TIP": "按下新的主用或备用下一武器键 / 转动滚轮 / 按 ESC 取消",
    # 英文: Previous Weapon -
    "GCID_PREVIOUSWEAPON": "上一武器 -",
    # 英文: Press Delete to clear / Select to change the Previous Weapon selection to another key, button or to the MouseWheel
    "GCID_PREVIOUSWEAPON_TIP": "按 Delete 清除 / 选择以更改切换上一武器键或按键",
    # 英文: Press the new primary or alternative Previous Weapon selection key, button or turn the MouseWheel / ESC to cancel
    "GCID_PREVIOUSWEAPON_CHANGE_TIP": "按下新的主用或备用上一武器键 / 转动滚轮 / 按 ESC 取消",
    # 英文: Select Best Weapon -
    "GCID_SELECTBESTWEAPON": "选择最佳武器 -",
    # 英文: Press Delete to clear / Select to change the Best Weapon selection key or button
    "GCID_SELECTBESTWEAPON_TIP": "按 Delete 清除 / 选择以更改选择最佳武器键或按键",
    # 英文: Press the new primary or alternative Best Weapon Available selection key or button / ESC to cancel
    "GCID_SELECTBESTWEAPON_CHANGE_TIP": "按下新的主用或备用最佳武器键 / 按 ESC 取消",
    # 英文: Select Sec. Attack -
    "GCID_MELEE": "选择副攻击 -",
    # 英文: Press Delete to clear / Select to change the Select Secondary Attack key or button
    "GCID_MELEE_TIP": "按 Delete 清除 / 选择以更改选择副攻击键或按键",
    # 英文: Press the new primary or alternative Secondary Attack selection key or button / ESC to cancel
    "GCID_MELEE_CHANGE_TIP": "按下新的主用或备用副攻击选择键 / 按 ESC 取消",
    # 英文: Select Handguns -
    "GCID_HANDGUNS": "选择手枪 -",
    # 英文: Press Delete to clear / Select to change the Handguns selection key or button
    "GCID_HANDGUNS_TIP": "按 Delete 清除 / 选择以更改选择手枪键或按键",
    # 英文: Press the new primary or alternative Handgun selection key or button / ESC to cancel
    "GCID_HANDGUNS_CHANGE_TIP": "按下新的主用或备用手枪选择键 / 按 ESC 取消",
    # 英文: Select Shotguns -
    "GCID_SHOTGUNS": "选择霰弹枪 -",
    # 英文: Press Delete to clear / Select to change the Shotguns selection key or button
    "GCID_SHOTGUNS_TIP": "按 Delete 清除 / 选择以更改选择霰弹枪键或按键",
    # 英文: Press the new primary or alternative Shotgun selection key or button / ESC to cancel
    "GCID_SHOTGUNS_CHANGE_TIP": "按下新的主用或备用霰弹枪选择键 / 按 ESC 取消",
    # 英文: Select SMGs -
    "GCID_MACHINEGUNS": "选择冲锋枪 -",
    # 英文: Press Delete to clear / Select to change the Submachineguns selection key or button
    "GCID_MACHINEGUNS_TIP": "按 Delete 清除 / 选择以更改选择冲锋枪键或按键",
    # 英文: Press the new primary or alternative Submachineguns  selection key or button / ESC to cancel
    "GCID_MACHINEGUNS_CHANGE_TIP": "按下新的主用或备用冲锋枪选择键 / 按 ESC 取消",
    # 英文: Select Assault Rifles -
    "GCID_RIFLES": "选择突击步枪 -",
    # 英文: Press Delete to clear / Select to change the Assault Rifles selection key or button
    "GCID_RIFLES_TIP": "按 Delete 清除 / 选择以更改选择突击步枪键或按键",
    # 英文: Press the new primary or alternative Assault Rifles selection key or button / ESC to cancel
    "GCID_RIFLES_CHANGE_TIP": "按下新的主用或备用突击步枪选择键 / 按 ESC 取消",
    # 英文: Select Sniper Rifles -
    "GCID_SNIPER": "选择狙击步枪 -",
    # 英文: Press Delete to clear / Select to change the Sniper Rifles selection key or button
    "GCID_SNIPER_TIP": "按 Delete 清除 / 选择以更改选择狙击步枪键或按键",
    # 英文: Press the new primary or alternative Sniper Rifle selection key or button / ESC to cancel
    "GCID_SNIPER_CHANGE_TIP": "按下新的主用或备用狙击步枪选择键 / 按 ESC 取消",
    # 英文: Mouse Settings
    "GCID_MOUSESETTINGS": "鼠标设置",
    # 英文: Modify or view mouse settings
    "GCID_MOUSESETTINGS_TIP": "修改或查看鼠标设置",
    # 英文: MOUSE SETTINGS
    "GCID_MOUSESETTINGSU": "鼠标设置",
    # 英文: Horizontal Aiming Speed
    "GCID_AIMINGHSPEED": "水平瞄准速度",
    # 英文: Use the cursor keys or mouse to change the horizontal aiming speed
    "GCID_AIMINGHSPEED_TIP": "用方向键或鼠标调整水平瞄准速度",
    # 英文: Vertical Aiming Speed
    "GCID_AIMINGVSPEED": "垂直瞄准速度",
    # 英文: Use the cursor keys or mouse to change the vertical aiming speed
    "GCID_AIMINGVSPEED_TIP": "用方向键或鼠标调整垂直瞄准速度",
    # 英文: Invert Mouse
    "GCID_INVERTMOUSE": "反转鼠标",
    # 英文: Toggle inverted vertical aiming movement for the mouse
    "GCID_INVERTMOUSE_TIP": "切换鼠标垂直瞄准的反转",
    # 英文: Restore Defaults
    "GCID_RESTOREDEFAULTS": "恢复默认",
    # 英文: Restore original default control settings
    "GCID_RESTOREDEFAULTS_TIP": "恢复默认操作设置",
    # 英文: Game
    "GCID_GENERIC": "游戏",
    # 英文: Modify or view the general gameplay options
    "GCID_GENERIC_TIP": "修改或查看通用游戏选项",
    # 英文: GAME
    "GCID_GENERICU": "游戏",
    # 英文: Select Crosshair
    "GCID_SELECTCROSSHAIR": "选择准星",
    # 英文: Select crosshair you wish to use
    "GCID_SELECTCROSSHAIR_TIP": "选择你想使用的准星",
    # 英文: SELECT CROSSHAIR
    "GCID_SELECTCROSSHAIRU": "选择准星",
    # 英文: Select between different aiming reticules
    "GCID_SHOWCROSSHAIR_TIP": "在不同的瞄准镜样式间选择",
    # 英文: White Dot
    "GCID_SHOWCROSSHAIR1": "白点",
    # 英文: White Circle
    "GCID_SHOWCROSSHAIR2": "白圈",
    # 英文: White Cross
    "GCID_SHOWCROSSHAIR3": "白十字",
    # 英文: Yellow Dot
    "GCID_SHOWCROSSHAIR4": "黄点",
    # 英文: Yellow Circle
    "GCID_SHOWCROSSHAIR5": "黄圈",
    # 英文: Yellow Cross
    "GCID_SHOWCROSSHAIR6": "黄十字",
    # 英文: Red Dot
    "GCID_SHOWCROSSHAIR7": "红点",
    # 英文: Red Circle
    "GCID_SHOWCROSSHAIR8": "红圈",
    # 英文: Red Cross
    "GCID_SHOWCROSSHAIR9": "红十字",
    # 英文: None
    "GCID_SHOWCROSSHAIR10": "无",
    # 英文: Enable Auto Aiming
    "GCID_ENABLEAUTOAIM": "开启自动瞄准",
    # 英文: Toggle Auto Aiming assistance
    "GCID_ENABLEAUTOAIM_TIP": "切换自动瞄准辅助",
    # 英文: Auto Weapon Change
    "GCID_AUTOWEAPONCHANGE": "自动切换武器",
    # 英文: Toggle Automatic Best Weapon Selection when picking up a new weapon
    "GCID_AUTOWEAPONCHANGE_TIP": "拾取新武器时自动选择最佳武器",
    # 英文: Enable Bullet Time Aid
    "GCID_BULLETTIMEAID": "开启子弹时间辅助",
    # 英文: Conserve as much Bullet Time as possible by automatically disabling Bullet Time in certain game play situations
    "GCID_BULLETTIMEAID_TIP": "在特定情况下自动关闭子弹时间，尽量节省",
    # 英文: Enable Subtitles
    "GCID_SUBTITLES": "开启字幕",
    # 英文: Toggle subtitles on and off
    "GCID_SUBTITLES_TIP": "开启或关闭字幕",
    # 英文: Read Story - F1
    "GCID_READSTORY": "阅读剧情 - F1",
    # 英文: Read the story you have played so far - the key-binding cannot be changed
    "GCID_READSTORY_TIP": "阅读至今所经历的剧情（按键绑定不可更改）",
    # 英文: Quick Save - F5
    "GCID_QUICKSAVE": "快速保存 - F5",
    # 英文: Save your current game in the quick save slot - the key-binding cannot be changed
    "GCID_QUICKSAVE_TIP": "将当前游戏存入快速存档槽（按键绑定不可更改）",
    # 英文: Quick Load - F9
    "GCID_QUICKLOAD": "快速读取 - F9",
    # 英文: Load the most recently used save game - the key-binding cannot be changed
    "GCID_QUICKLOAD_TIP": "读取最近使用的存档（按键绑定不可更改）",
    # 英文: Video
    "GCID_VIDEO": "画面",
    # 英文: Modify or view the video settings
    "GCID_VIDEO_TIP": "修改或查看画面设置",
    # 英文: VIDEO
    "GCID_VIDEOU": "画面",
    # 英文: Texture Sharpness
    "GCID_TEXTUREMIPMAP": "纹理锐度",
    # 英文: Use the cursor keys or mouse to adjust texture sharpness (ie. mipmap bias)
    "GCID_TEXTUREMIPMAP_TIP": "用方向键或鼠标调整纹理锐度（即贴图偏移）",
    # 英文: Brightness
    "GCID_GAMMACONTROL": "亮度",
    # 英文: Use the cursor keys or mouse to adjust brightness
    "GCID_GAMMACONTROL_TIP": "用方向键或鼠标调整亮度",
    # 英文: Audio
    "GCID_SOUND": "音频",
    # 英文: Modify or view the audio settings
    "GCID_SOUND_TIP": "修改或查看音频设置",
    # 英文: AUDIO
    "GCID_SOUNDU": "音频",
    # 英文: Music Volume
    "GCID_MUSICVOLUME": "音乐音量",
    # 英文: Use the cursor keys or mouse to adjust the music volume
    "GCID_MUSICVOLUME_TIP": "用方向键或鼠标调整音乐音量",
    # 英文: Effects Volume
    "GCID_EFFECTSVOLUME": "音效音量",
    # 英文: Use the cursor keys or mouse to adjust the sound effects volume
    "GCID_EFFECTSVOLUME_TIP": "用方向键或鼠标调整音效音量",
    # 英文: Last attempt %s Record %s
    "GCID_NYMTIMES": "上次成绩 %s  纪录 %s",
    # 英文: NEW RECORD %s
    "GCID_NYMNEWRECORD": "新纪录 %s",
    # 英文: Still running... Select to continue
    "GCID_NYMSTILLRUNNING": "仍在继续……选择以继续",
    # 英文: Dead Man Walking
    "GCID_SURVIVALMODE": "死囚漫步",
    # 英文: Death is inevitable. How long will you last?
    "GCID_SURVIVALMODE_TIP": "死亡无可避免。你能撑多久？",
    # 英文: Out in the night madness lay in ambush, waiting for me.
    "GCID_QUITJOKE01": "                                  夜色中的疯狂潜伏在暗处，等候着我。",
    # 英文: Rain had washed away the trail ahead.
    "GCID_QUITJOKE02": "                                  雨水洗去了前方的踪迹。",
    # 英文: I hadn't been able to crack the case.
    "GCID_QUITJOKE03": "                                  我始终没能破解这桩案子。",
    # 英文: I had lost my way.
    "GCID_QUITJOKE04": "                                  我迷失了方向。",
    # 英文: The mystery I was chasing wore my own face.
    "GCID_QUITJOKE05": "                                  我所追逐的谜团，戴着我的那张脸。",
    # 英文: The asphalt shivered restlessly under my feet.
    "GCID_QUITJOKE06": "                                  沥青在我脚下不安地战栗。",
    # 英文: A labyrinth of dark streets spread before me.
    "GCID_QUITJOKE07": "                                  一座由黑暗街道织成的迷宫在我眼前铺开。",
    # 英文: I felt numb. I was dead inside.
    "GCID_QUITJOKE08": "                                  我感到麻木。我的内心已经死去。",
    # 英文: With each gunshot, my case grew more complex.
    "GCID_QUITJOKE09": "                                  每一声枪响，都让我的案子更加复杂。",
    # 英文: The city was an insomniac. Like me.
    "GCID_QUITJOKE10": "                                  这座城市像我一样失眠。",
    # 英文: The mystery leered at me, ugly in the mirror.
    "GCID_QUITJOKE11": "                                  谜团在镜中冲我狞笑，丑陋不堪。",
    # 英文: All my choices turned to catastrophes in the past tense.
    "GCID_QUITJOKE12": "                                  我所有的选择，都变成了过去时态的灾难。",
    # 英文: I caught glimpses of the dead out of the corner of my eye.
    "GCID_QUITJOKE13": "                                  眼角余光里，我瞥见死者的身影。",
    # 英文: The dead kept whispering to me from six feet under.
    "GCID_QUITJOKE14": "                                  逝者从六尺之下，不断向我低语。",
    # 英文: My death waited in the darkness of every gun barrel.
    "GCID_QUITJOKE15": "                                  我的死亡，潜伏在每根枪管的黑暗里。",
    # 英文: Truth and free will are lies you tell yourself to sleep at night.
    "GCID_QUITJOKE16": "                                  真相与自由意志，不过是你哄自己入睡的谎言。",
    # 英文: My obsessions were making my choices for me.
    "GCID_QUITJOKE17": "                                  是我的执念，替我做着选择。",
    # 英文: Right and wrong were just hollow fictions.
    "GCID_QUITJOKE18": "                                  对与错，只是空洞的虚构。",
    # 英文: I looked for answers, but each gunshot was just a new question.
    "GCID_QUITJOKE19": "                                  我寻找答案，可每一声枪响都只是新的疑问。",
    # 英文: The storm was working itself into a fever pitch.
    "GCID_QUITJOKE20": "                                  风暴正酝酿到沸腾的顶点。",
    # 英文: The night went on, endless before me.
    "GCID_QUITJOKE21": "                                  长夜无尽，在我面前延伸。",
    # 英文: The city stared at me with sharp neon eyes.
    "GCID_QUITJOKE22": "                                  城市用锐利的霓虹之眼盯着我。",
    # 英文: Under my jacket, the pistol dug painfully into my side.
    "GCID_QUITJOKE23": "                                  外套之下，手枪狠狠硌着我的腰侧。",
    # 英文: Every gunshot was just a hole with more questions leaking out.
    "GCID_QUITJOKE24": "                                  每一声枪响，都只是个漏出更多疑问的洞。",
    # 英文: I stood in the heart of a spreading labyrinth of questions.
    "GCID_QUITJOKE25": "                                  我伫立在不断扩张的疑问迷宫中央。",
    # 英文: The shadows of the city pressed close, suffocating.
    "GCID_QUITJOKE26": "                                  城市的阴影逼近，令人窒息。",
    # 英文: I could hear the monstrous heartbeat of the city under my feet.
    "GCID_QUITJOKE27": "                                  我能听见城市巨兽般的心跳，就在脚下。",
    # 英文: The case was a rising nausea that tasted like rust in my mouth.
    "GCID_QUITJOKE28": "                                  这桩案子像一阵不断上涌的恶心，嘴里满是铁锈味。",
    # 英文: The night of New York City had only begun.
    "GCID_QUITJOKE29": "                                  纽约市的夜晚，才刚刚开始。",
    # 英文: There were no answers to my questions.
    "GCID_QUITJOKE30": "                                  我的疑问，没有答案。",
    # 英文: All the reasons were mysteries, hiding in the dark.
    "GCID_QUITJOKE31": "                                  所有的理由都是谜团，藏在黑暗里。",
    # 英文: The city was a necropolis, hungry for more corpses.
    "GCID_QUITJOKE32": "                                  这座城市是片亡灵之地，渴望更多尸体。",
    # 英文: The rain outside made cadavers grow from bullet seeds.
    "GCID_QUITJOKE33": "                                  外面的雨，让子弹的种子长出了尸体。",
    # 英文: I knew the dreamless dreams and hopeless hopes of the dead.
    "GCID_QUITJOKE34": "                                  我懂得死者无梦的梦，与无望的望。",
    # 英文: I had a crazy, desperate feeling about Mona.
    "GCID_QUITJOKE35": "                                  对莫娜，我有一种疯狂而绝望的感觉。",
    # 英文: Only a fool falls for a woman who puts a gun to your face.
    "GCID_QUITJOKE36": "                                  只有傻子，才会爱上把枪口对准你脸的女人。",
    # 英文: It would take a first-degree fool to fall for a dead woman.
    "GCID_QUITJOKE37": "                                  爱上死去的女人，得是头号傻子才行。",
    # 英文: My death had an unfair advantage, unlimited ammo.
    "GCID_QUITJOKE38": "                                  我的死亡占着不公的优势——弹药无限。",
    # 英文: My death grinned at me in the mirror.
    "GCID_QUITJOKE39": "                                  我的死亡在镜子里冲我咧嘴一笑。",
    # 英文: I felt old and tired, I didn't recognize my face in the mirror.
    "GCID_QUITJOKE40": "                                  我感到苍老而疲惫，镜中的脸已认不出自己。",
    # 英文: The night seemed to stretch on to eternity.
    "GCID_QUITJOKE41": "                                  长夜仿佛延伸到永恒。",
    # 英文: I was stranded in darkness. The sun had given up on me.
    "GCID_QUITJOKE42": "                                  我困在黑暗里。太阳早已放弃了我。",
    # 英文: The storm had grown to a vertical rain of bullets.
    "GCID_QUITJOKE43": "                                  风暴已化作垂直落下的弹雨。",
    # 英文: Death kept writing me valentines in blood.
    "GCID_QUITJOKE44": "                                  死亡不停地用鲜血给我写情书。",
    # 英文: I felt temptation to lose myself into the night.
    "GCID_QUITJOKE45": "                                  我忍不住想把自己沉入这夜色。",
    # 英文: My shield made me feel like a vampire wearing a cross.
    "GCID_QUITJOKE46": "                                  我的护盾让我像个挂着十字架的吸血鬼。",
    # 英文: The map of the city looked like the photo of my face.
    "GCID_QUITJOKE47": "                                  城市的地图，像极了我脸的照片。",
    # 英文: The gun felt fused to my hand.
    "GCID_QUITJOKE48": "                                  枪仿佛焊在了我手上。",
    # 英文: No amount of painkillers could keep this ache away.
    "GCID_QUITJOKE49": "                                  再多的止痛药，也压不住这阵痛楚。",
    # 英文: The night was as dark as a bullet hole.
    "GCID_QUITJOKE50": "                                  夜色如弹孔般漆黑。",
    # 英文: I was afraid to go on.
    "GCID_QUIT_YES": "                                  我害怕继续走下去。",
    # 英文: But I refused to give in. I had to continue.
    "GCID_QUIT_NO": "                                  但我拒绝屈服。我必须继续。",
    # 英文: Are you sure?
    "GCID_AREYOUSURE": "你确定吗？",
    # 英文: Yes
    "GCID_YES": "是",
    # 英文: Accept changes
    "GCID_YES_TIP": "接受更改",
    # 英文: No
    "GCID_NO": "否",
    # 英文: Cancel changes
    "GCID_NO_TIP": "取消更改",
    # 英文: Back
    "GCID_BACK": "返回",
    # 英文: Back to the previous page
    "GCID_BACK_TIP": "返回上一页",
    # 英文: Quit your current game and exit to the desktop
    "GCID_QUIT_YES_TIP": "退出当前游戏并返回桌面",
    # 英文: Return to the main menu
    "GCID_QUIT_NO_TIP": "返回主菜单",
    # ---- 关卡标题卡 / 章节名 (LNID) ----
    # 英文: Manor Yard
    "LNID_SURVIVALMODE_MAP1": "庄园庭院",
    # 英文: Construction Site
    "LNID_SURVIVALMODE_MAP2": "建筑工地",
    # 英文: Manor Garden
    "LNID_SURVIVALMODE_MAP3": "庄园花园",
    # 英文: Used Car Lot
    "LNID_SURVIVALMODE_MAP4": "戈尼提的地盘",
    # 英文: Scaffolding
    "LNID_SURVIVALMODE_MAP5": "脚手架",
    # 英文: Part I
    "LNID_PART1": "第一部分",
    # 英文: PART I
    "LNID_PART1_U": "第一部分",
    # 英文: Part I, Prologue
    "LNID_PART1_PROLOGUE": "第一部分，序章",
    # 英文: Part I, Chapter 1
    "LNID_PART1_CHAPTER1": "第一部分·第一章",
    # 英文: Part I, Chapter 2
    "LNID_PART1_CHAPTER2": "第一部分·第二章",
    # 英文: Part I, Chapter 3
    "LNID_PART1_CHAPTER3": "第一部分·第三章",
    # 英文: Part I, Chapter 4
    "LNID_PART1_CHAPTER4": "第一部分·第四章",
    # 英文: Part I, Chapter 5
    "LNID_PART1_CHAPTER5": "第一部分·第五章",
    # 英文: Part I, Chapter 6
    "LNID_PART1_CHAPTER6": "第一部分·第六章",
    # 英文: Part I, Chapter 7
    "LNID_PART1_CHAPTER7": "第一部分·第七章",
    # 英文: Part II
    "LNID_PART2": "第二部分",
    # 英文: PART II
    "LNID_PART2_U": "第二部分",
    # 英文: Part II, Prologue
    "LNID_PART2_PROLOGUE": "第二部分，序章",
    # 英文: Part II, Chapter 1
    "LNID_PART2_CHAPTER1": "第二部分·第一章",
    # 英文: Part II, Chapter 2
    "LNID_PART2_CHAPTER2": "第二部分·第二章",
    # 英文: Part II, Chapter 3
    "LNID_PART2_CHAPTER3": "第二部分·第三章",
    # 英文: Part II, Chapter 4
    "LNID_PART2_CHAPTER4": "第二部分·第四章",
    # 英文: Part II, Chapter 5
    "LNID_PART2_CHAPTER5": "第二部分·第五章",
    # 英文: Part II, Chapter 6
    "LNID_PART2_CHAPTER6": "第二部分·第六章",
    # 英文: Part III
    "LNID_PART3": "第三部分",
    # 英文: PART III
    "LNID_PART3_U": "第三部分",
    # 英文: Part III, Prologue
    "LNID_PART3_PROLOGUE": "第三部分，序章",
    # 英文: Part III, Chapter 1
    "LNID_PART3_CHAPTER1": "第三部分·第一章",
    # 英文: Part III, Chapter 2
    "LNID_PART3_CHAPTER2": "第三部分·第二章",
    # 英文: Part III, Chapter 3
    "LNID_PART3_CHAPTER3": "第三部分·第三章",
    # 英文: Part III, Chapter 4
    "LNID_PART3_CHAPTER4": "第三部分·第四章",
    # 英文: Part III, Chapter 5
    "LNID_PART3_CHAPTER5": "第三部分·第五章",
    # 英文: Part III, Chapter 6
    "LNID_PART3_CHAPTER6": "第三部分·第六章",
    # 英文: Part III, Chapter 7
    "LNID_PART3_CHAPTER7": "第三部分·第七章",
    # 英文: Part III, Chapter 8
    "LNID_PART3_CHAPTER8": "第三部分·第八章",
    # 英文: Prologue
    "LNID_PROLOGUE": "序章",
    # 英文: Chapter One
    "LNID_CHAPTER1": "第一章",
    # 英文: Chapter Two
    "LNID_CHAPTER2": "第二章",
    # 英文: Chapter Three
    "LNID_CHAPTER3": "第三章",
    # 英文: Chapter Four
    "LNID_CHAPTER4": "第四章",
    # 英文: Chapter Five
    "LNID_CHAPTER5": "第五章",
    # 英文: Chapter Six
    "LNID_CHAPTER6": "第六章",
    # 英文: Chapter Seven
    "LNID_CHAPTER7": "第七章",
    # 英文: Chapter Eight
    "LNID_CHAPTER8": "第八章",
    # 英文: The Darkness Inside
    "LNID_PART1_TIP": "心中的黑暗",
    # 英文: Prologue (Hospital)
    "LNID_PART1_PROLOGUE_TIP": "序章（医院）",
    # 英文: Elevator Doors (Vlad's Warehouse)
    "LNID_PART1_CHAPTER1_TIP": "电梯之门（弗拉德的仓库）",
    # 英文: A Criminal Mastermind (Vlad's Restaurant)
    "LNID_PART1_CHAPTER2_TIP": "犯罪首脑（弗拉德的餐厅）",
    # 英文: The Depths of My Brain (Max's 1st Nightmare)
    "LNID_PART1_CHAPTER3_TIP": "脑海深处（马克思的第一次噩梦）",
    # 英文: No 'Us' in This (Max's Apartment Building)
    "LNID_PART1_CHAPTER4_TIP": "没有“我们”这回事（马克思的公寓楼）",
    # 英文: A Sign of Her Passage (Max's Apartment Building cont'd)
    "LNID_PART1_CHAPTER5_TIP": "她留下的痕迹（马克思的公寓楼·续）",
    # 英文: A Linear Sequence of Scares (Mona's Funhouse)
    "LNID_PART1_CHAPTER6_TIP": "一连串惊吓（莫娜的游乐屋）",
    # 英文: The Million Dollar Question (Upper East Side Apartment Building)
    "LNID_PART1_CHAPTER7_TIP": "百万美元的问题（上东区公寓楼）",
    # 英文: A Binary Choice
    "LNID_PART2_TIP": "非此即彼",
    # 英文: Prologue (Police Station)
    "LNID_PART2_PROLOGUE_TIP": "序章（警察局）",
    # 英文: The Things that I Want (Return to Mona's Funhouse)
    "LNID_PART2_CHAPTER1_TIP": "我心之所向（重返莫娜的游乐屋）",
    # 英文: In the Middle of Something (Condemned Building)
    "LNID_PART2_CHAPTER2_TIP": "左右为难（危楼）",
    # 英文: Blowing Up (Condemned Building cont'd)
    "LNID_PART2_CHAPTER3_TIP": "引爆（危楼·续）",
    # 英文: Routing Her Synapses (Construction Site, as Mona)
    "LNID_PART2_CHAPTER4_TIP": "操控她的神经突触（建筑工地，扮演莫娜）",
    # 英文: Out of the Window (Construction Site cont'd, as Mona)
    "LNID_PART2_CHAPTER5_TIP": "破窗而出（建筑工地·续，扮演莫娜）",
    # 英文: The Genius of the Hole (Construction Site cont'd, as Mona)
    "LNID_PART2_CHAPTER6_TIP": "深渊的诡计（建筑工地·续，扮演莫娜）",
    # 英文: Waking Up from the American Dream
    "LNID_PART3_TIP": "从美国梦中醒来",
    # 英文: Prologue (Max's 2nd Nightmare)
    "LNID_PART3_PROLOGUE_TIP": "序章（马克思的第二次噩梦）",
    # 英文: Too Stubborn to Die (Hospital cont'd)
    "LNID_PART3_CHAPTER1_TIP": "顽强不死（医院·续）",
    # 英文: On a Crash Course (Return to Vlad's Restaurant)
    "LNID_PART3_CHAPTER2_TIP": "迎头相撞（重返弗拉德的餐厅）",
    # 英文: A Mob-War (Slum Neighborhood)
    "LNID_PART3_CHAPTER3_TIP": "帮派火并（贫民区）",
    # 英文: Dearest of All My Friends (Vinnie's Used Car Lot)
    "LNID_PART3_CHAPTER4_TIP": "最亲爱的朋友（维尼的二手车场）",
    # 英文: A Losing Game (Return to Funhouse, as Mona)
    "LNID_PART3_CHAPTER5_TIP": "必输的赌局（重返游乐屋，扮演莫娜）",
    # 英文: There Are No Happy Endings (Max's 3rd Nightmare)
    "LNID_PART3_CHAPTER6_TIP": "没有圆满的结局（马克思的第三次噩梦）",
    # 英文: Love Hurts (Woden's Manor)
    "LNID_PART3_CHAPTER7_TIP": "爱的痛苦（沃登的庄园）",
    # 英文: That Old Familiar Feeling (Woden's Manor cont'd)
    "LNID_PART3_CHAPTER8_TIP": "那熟悉的旧感觉（沃登的庄园·续）",
    # ---- 游戏内 HUD 提示 (SGID) ----
    # 英文: Game loaded
    "SGID_LOADHUDTEXT": "游戏已载入",
    # 英文: Game saved
    "SGID_SAVEHUDTEXT": "游戏已保存",
    # 英文: Game saved - %i saves left
    "SGID_SAVELIMITEDHUDTEXT": "游戏已保存 — 剩余存档 %i 次",
    # 英文: Game not saved! No saves left
    "SGID_UNABLETOSAVEHUDTEXT": "未能保存！存档次数已用尽",
    # 英文: No game to load
    "SGID_SAVEGAMENOTFOUNDHUDTEXT": "没有可读取的存档",
    # 英文: Could not save game at this point
    "SGID_CANNOTSAVEHUDTEXT": "当前位置无法保存",
    # 英文: Unable to write save game file - game not saved
    "SGID_SAVINGFAILEDHUDTEXT": "无法写入存档文件 — 游戏未保存",
    # 英文: You ran out of time!
    "SGID_OUTOFTIME": "时间耗尽！",
    # ---- 影像 / 暂停提示 (GNID) ----
    # 英文: Previous Chapter
    "GNID_TIP_PREVIOUS_CHAPTER": "上一章",
    # 英文: Previous Page
    "GNID_TIP_PREVIOUS_PAGE": "上一页",
    # 英文: Play
    "GNID_TIP_PLAY": "播放",
    # 英文: Stop
    "GNID_TIP_STOP": "停止",
    # 英文: Next Page
    "GNID_TIP_NEXT_PAGE": "下一页",
    # 英文: Next Chapter
    "GNID_TIP_NEXT_CHAPTER": "下一章",
    # 英文: Back to Game
    "GNID_TIP_QUIT": "返回游戏",
    # 英文: Paused
    "GNID_PAUSE": "已暂停",
}

HUD = {
    # 英文: +2 sec
    "HUDPRINT_SURVIVAL_KILL": "+2 秒",
    # 英文: 9mm Pistol Ammo
    "HUDPRINT_PICKUP_BERETTA_AMMO": "九毫米手枪弹药",
    # 英文: Desert Eagle Ammo
    "HUDPRINT_PICKUP_DESERTEAGLE_AMMO": "沙漠之鹰弹药",
    # 英文: Shotgun Ammo
    "HUDPRINT_PICKUP_SHOTGUN_AMMO": "霰弹枪弹药",
    # 英文: Striker Ammo
    "HUDPRINT_PICKUP_STRIKER_AMMO": "打击者弹药",
    # 英文: Ingram Ammo
    "HUDPRINT_PICKUP_INGRAM_AMMO": "英格拉姆弹药",
    # 英文: MP5 Ammo
    "HUDPRINT_PICKUP_MP5_AMMO": "MP5弹药",
    # 英文: Kalashnikov Ammo
    "HUDPRINT_PICKUP_KALASHNIKOV_AMMO": "卡拉什尼科夫弹药",
    # 英文: M4 Carbine Ammo
    "HUDPRINT_PICKUP_COLTCOMMANDO_AMMO": "M4卡宾枪弹药",
    # 英文: Sniper Rifle Ammo
    "HUDPRINT_PICKUP_SNIPER_AMMO": "狙击步枪弹药",
    # 英文: Dragunov Ammo
    "HUDPRINT_PICKUP_DRAGUNOV_AMMO": "德拉贡诺夫弹药",
    # 英文: 9mm Pistol
    "HUDPRINT_PICKUP_BERETTA": "九毫米手枪",
    # 英文: 9mm Pistol
    "HUDPRINT_PICKUP_BERETTADUAL": "九毫米手枪",
    # 英文: Desert Eagle
    "HUDPRINT_PICKUP_DESERTEAGLE": "沙漠之鹰",
    # 英文: Sawed-Off Shotgun
    "HUDPRINT_PICKUP_SAWEDSHOTGUN": "锯短型霰弹枪",
    # 英文: Pump-Action Shotgun
    "HUDPRINT_PICKUP_PUMPSHOTGUN": "泵动式霰弹枪",
    # 英文: Striker
    "HUDPRINT_PICKUP_STRIKER": "打击者",
    # 英文: Ingram
    "HUDPRINT_PICKUP_INGRAM": "英格拉姆",
    # 英文: Ingram
    "HUDPRINT_PICKUP_INGRAMDUAL": "英格拉姆",
    # 英文: MP5
    "HUDPRINT_PICKUP_MP5": "MP5",
    # 英文: Kalashnikov
    "HUDPRINT_PICKUP_KALASHNIKOV": "卡拉什尼科夫",
    # 英文: M4 Carbine
    "HUDPRINT_PICKUP_COLTCOMMANDO": "M4卡宾枪",
    # 英文: Sniper Rifle
    "HUDPRINT_PICKUP_SNIPER": "狙击步枪",
    # 英文: Dragunov
    "HUDPRINT_PICKUP_DRAGUNOV": "德拉贡诺夫",
    # 英文: Painkillers
    "HUDPRINT_PICKUP_PAINKILLERS": "止痛药",
    # 英文: Molotov Cocktail
    "HUDPRINT_PICKUP_MOLOTOV": "燃烧瓶",
    # 英文: Grenade
    "HUDPRINT_PICKUP_GRENADE": "手榴弹",
    # 英文: 9mm Pistol Ammo full
    "HUDPRINT_PICKUP_BERETTA_AMMO_FULL": "九毫米手枪弹药已满",
    # 英文: Desert Eagle Ammo full
    "HUDPRINT_PICKUP_DESERTEAGLE_AMMO_FULL": "沙漠之鹰弹药已满",
    # 英文: Shotgun Ammo full
    "HUDPRINT_PICKUP_SHOTGUN_AMMO_FULL": "霰弹枪弹药已满",
    # 英文: Striker Ammo full
    "HUDPRINT_PICKUP_STRIKER_AMMO_FULL": "打击者弹药已满",
    # 英文: Ingram Ammo full
    "HUDPRINT_PICKUP_INGRAM_AMMO_FULL": "英格拉姆弹药已满",
    # 英文: MP5 Ammo full
    "HUDPRINT_PICKUP_MP5_AMMO_FULL": "MP5弹药已满",
    # 英文: Kalashnikov Ammo full
    "HUDPRINT_PICKUP_KALASHNIKOV_AMMO_FULL": "卡拉什尼科夫弹药已满",
    # 英文: M4 Carbine Ammo full
    "HUDPRINT_PICKUP_COLTCOMMANDO_AMMO_FULL": "M4卡宾枪弹药已满",
    # 英文: Sniper Ammo full
    "HUDPRINT_PICKUP_SNIPER_AMMO_FULL": "狙击步枪弹药已满",
    # 英文: Dragunov Ammo full
    "HUDPRINT_PICKUP_DRAGUNOV_AMMO_FULL": "德拉贡诺夫弹药已满",
    # 英文: Painkillers full
    "HUDPRINT_PICKUP_PAINKILLERS_FULL": "止痛药已满",
    # 英文: Molotovs full
    "HUDPRINT_PICKUP_MOLOTOV_AMMO_FULL": "燃烧瓶已满",
    # 英文: Grenades full
    "HUDPRINT_PICKUP_GRENADE_AMMO_FULL": "手榴弹已满",
    # 英文: Paused
    "NoPauseCameraPathText": "已暂停",
    # 英文: Quick:
    "QuickSaveGameDescriptionPrefix": "快速：",
    # 英文: Auto:
    "AutoSaveGameDescriptionPrefix": "自动：",
    # 英文: Press F9 again to Quickload, Esc to Cancel
    "QuickLoadQueryText": "再次按 F9 快速读取，按 Esc 取消",
    # 英文: Press the use key (#USE#) to load the last saved game.
    "HUDPRINT_PRESS_USE_TO_LOAD": "按使用键（#USE#）载入最近的存档。",
    # 英文: Press the quickload key (F9) to load the last saved game.
    "HUDPRINT_PRESS_F9_TO_LOAD": "按快速读取键（F9）载入最近的存档。",
    # 英文: Tip: Press #PAUSE# to switch off the pause mode.
    "TIP_PAUSECAMERA": "提示：按 #PAUSE# 关闭暂停模式。",
    # 英文: Tip: Press and hold the use key (#USE#) to zoom with the sniper rifle.
    "TIP_SNIPER": "提示：按住使用键（#USE#）用狙击步枪缩放。",
    # 英文: Tip: Press #PAINKILLER# to use painkillers to ease the pain.
    "TIP_PAINKILLER": "提示：按 #PAINKILLER# 使用止痛药缓解疼痛。",
    # 英文: Tip: Press the use key (#USE#) to use or examine interesting items.
    "TIP_EXAMINE": "提示：按使用键（#USE#）使用或检视有趣物品。",
    # 英文: Tip: Press ShootDodge key (#DODGEMODIFIER#) and direction to shootdodge.
    "TIP_SHOOTDODGE": "提示：按翻滚闪避键（#DODGEMODIFIER#）加方向进行翻滚闪避。",
    # 英文: Tip: Press Bullet Time (#SLOWMOTION#) to go into Bullet Time.
    "TIP_BULLETTIME": "提示：按子弹时间（#SLOWMOTION#）进入子弹时间。",
    # 英文: Tip: Press #JUMP# and a direction key to perform evasive rolls.
    "TIP_DODGE": "提示：按 #JUMP# 加方向键进行闪避翻滚。",
    # 英文: Congratulations! You have completed Max Payne 2: The Fall of Max Payne.
    "STRING_NORMAL_COMPLETED1": "恭喜！你已通关《马克思·佩恩2：马克思·佩恩的堕落》。",
    # 英文: The Dead Man Walking and New York Minute gameplay modes and
    "STRING_NORMAL_COMPLETED2": "“死囚漫步”与“纽约分钟”模式，以及",
    # 英文: Hard-Boiled difficulty level have been unlocked for even further challenges.
    "STRING_NORMAL_COMPLETED3": "“铁血”难度已解锁，迎接更多挑战。",
    # 英文: Congratulations!
    "STRING_NIGHTMARE_COMPLETED1": "恭喜！",
    # 英文: You have completed Hard-Boiled mode. Now prepare for
    "STRING_NIGHTMARE_COMPLETED2": "你已通关“铁血”模式。现在准备迎接",
    # 英文: the ultimate challenge of Dead on Arrival gameplay mode.
    "STRING_NIGHTMARE_COMPLETED3": "“到院即死”模式的终极挑战。",
    # 英文: Congratulations!
    "STRING_HELL_COMPLETED1": "恭喜！",
    # 英文: You have completed Dead on Arrival -
    "STRING_HELL_COMPLETED2": "你已通关“到院即死”——",
    # 英文: the hardest challenge of them all.
    "STRING_HELL_COMPLETED3": "最艰难的挑战。",
    # 英文: Your current time is: #TOTALTIME#
    "STRING_NYM_MAP": "你的当前时间：#TOTALTIME#",
    # 英文: Remedy par at this point: 0:16:19
    "STRING_NYM_PART1_PAR": "此处 Remedy 标准时间：0:16:19",
    # 英文: Remedy par at this point: 0:27:41
    "STRING_NYM_PART2_PAR": "此处 Remedy 标准时间：0:27:41",
    # 英文: Congratulations! New York Minute Completed -
    "STRING_TIMEDMODE_COMPLETED1": "恭喜！纽约分钟模式通关——",
    # 英文: You have won the race against clock.
    "STRING_TIMEDMODE_COMPLETED2": "你赢得了与时间的赛跑。",
    # 英文: Your Total time was #TOTALTIME#
    "STRING_TIMEDMODE_COMPLETED3": "你的总时间：#TOTALTIME#",
    # 英文: Remedy par time is: 0:46:29
    "STRING_TIMEDMODE_COMPLETED4": "Remedy 标准时间：0:46:29",
}
