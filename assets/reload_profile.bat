@echo off
call netname.bat
set profile_path=%~dp0wifi-profile.xml
netsh wlan add profile filename="%profile_path%"
netsh wlan connect name="%netname%"