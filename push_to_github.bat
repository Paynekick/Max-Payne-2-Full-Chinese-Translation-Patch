@echo off
chcp 65001 >nul 2>&1
setlocal

REM ===== EDIT THESE TWO LINES BEFORE FIRST RUN =====
set "REMOTE_URL=https://github.com/Paynekick/Max-Payne-2-Full-Chinese-Translation-Patch.git"
set "GIT_NAME=Paynekick"
set "GIT_EMAIL=paynekick@users.noreply.github.com"
REM =================================================

cd /d "C:\Users\Paynekick\WorkBuddy\2026-08-09-13-13-05\Max-Payne-2-Full-Chinese-Translation-Patch"

if "%REMOTE_URL%"=="https://github.com/PASTE_YOUR_NAME/PASTE_REPO.git" (
    echo [X] You have not set REMOTE_URL yet. Open this file and edit the top lines.
    pause
    exit /b 1
)

git init
git config user.name "%GIT_NAME%"
git config user.email "%GIT_EMAIL%"
git add .
git commit -m "Initial release: Max Payne 2 Simplified Chinese patch (tool + sources)"
git branch -M main
git remote get-url origin >nul 2>&1 && git remote set-url origin "%REMOTE_URL%" || git remote add origin "%REMOTE_URL%"
git push -u origin main

pause
