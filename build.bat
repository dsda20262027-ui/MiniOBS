@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>&1
if errorlevel 1 (
    echo Python Launcher (py) not found.
    echo Install Python from python.org and enable "Add Python to PATH".
    pause
    exit /b 1
)

py -m pip install --upgrade pyinstaller
if errorlevel 1 (
    echo Failed to install PyInstaller.
    pause
    exit /b 1
)

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
mkdir build

py -m PyInstaller --noconfirm --clean --onefile --windowed --name MiniOBS src\mini_obs.py
if errorlevel 1 (
    echo EXE build failed.
    pause
    exit /b 1
)

copy /Y dist\MiniOBS.exe build\MiniOBS.exe >nul
echo.
echo OK: build\MiniOBS.exe
echo.
echo Now open installer\MiniOBS.iss in Inno Setup and click Build.
pause
