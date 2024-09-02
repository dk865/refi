@echo off
echo Creating Persistence...

if not exist X:\refi\ assets\ mkdir X:\refi
if not exist X:\refi\assets\ mkdir X:\refi\assets\

copy refi.exe X:\refi\refi.exe
xcopy assets\ X:\refi\assets\ /E /I /Y
copy X:\refi\assets\executables\refi-run.exe X:\Windows\system32\refi-run.exe
copy X:\refi\assets\executables\refi.exe X:\Windows\system32\refi.exe

echo Done.
timeout /t 3 >nul
exit
