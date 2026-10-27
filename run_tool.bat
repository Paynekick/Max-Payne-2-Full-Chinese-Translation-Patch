@echo off
REM Max Payne 2 Chinese Patch tool launcher (ASCII only to avoid codepage issues)
REM Requires Python 3.8+ ; first run: pip install pillow
where py >nul 2>nul
if %errorlevel%==0 (
  py mp2_translation_tool.py
) else (
  python mp2_translation_tool.py
)
pause
