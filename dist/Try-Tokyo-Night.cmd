@echo off
setlocal
set "VLC_EXE=%ProgramFiles%\VideoLAN\VLC\vlc.exe"
if not exist "%VLC_EXE%" set "VLC_EXE=%ProgramFiles(x86)%\VideoLAN\VLC\vlc.exe"
if not exist "%VLC_EXE%" (
  echo VLC was not found. Open VLC Preferences and select the VLT file manually.
  pause
  exit /b 1
)
start "" "%VLC_EXE%" --no-one-instance --no-save-config --intf=skins2 --skins2-last="%~dp0Tokyo-Night-Dark.vlt" %*
