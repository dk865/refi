@echo off
echo Removing Persistence...

del X:\refi\refi.exe
rmdir /S /Q X:\refi\assets\
rmdir /S /Q X:\refi\

del X:\Windows\system32\refi-run.exe
del X:\Windows\system32\refi.exe

echo Done.
timeout /t 3 >nul
exit
