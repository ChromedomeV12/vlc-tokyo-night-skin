@echo off
setlocal
set "VLC_EXE=%ProgramFiles%\VideoLAN\VLC\vlc.exe"
if not exist "%VLC_EXE%" set "VLC_EXE=%ProgramFiles(x86)%\VideoLAN\VLC\vlc.exe"
if not exist "%VLC_EXE%" (
  echo VLC was not found.
  pause
  exit /b 1
)
set "PRESETS=%~dp0visualizations"
if not exist "%PRESETS%\Tokyo Night - Waves.milk" set "PRESETS=%~dp0..\visualizations"
start "" "%VLC_EXE%" --no-one-instance --intf=skins2 --skins2-last="%~dp0Tokyo-Night-Dark.vlt" --audio-visual=projectm --projectm-preset-path="%PRESETS%" --projectm-texture-size=512 %*
