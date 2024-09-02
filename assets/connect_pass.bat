@echo off
echo Deleting Old Profile (If Exists)
del wifi-profile.xml
echo Creating WiFi Profile...
set profile_path=%~dp0wifi-profile.xml
echo Creating Wi-Fi profile XML file...
echo ^<?xml version="1.0"?^> > "%profile_path%"
echo ^<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"^> >> "%profile_path%"
echo     ^<name^>%1^</name^> >> "%profile_path%"
echo     ^<SSIDConfig^> >> "%profile_path%"
echo         ^<SSID^> >> "%profile_path%"
echo             ^<name^>%1^</name^> >> "%profile_path%"
echo         ^</SSID^> >> "%profile_path%"
echo     ^</SSIDConfig^> >> "%profile_path%"
echo     ^<connectionType^>ESS^</connectionType^> >> "%profile_path%"
echo     ^<connectionMode^>auto^</connectionMode^> >> "%profile_path%"
echo     ^<MSM^> >> "%profile_path%"
echo         ^<security^> >> "%profile_path%"
echo             ^<authEncryption^> >> "%profile_path%"
echo                 ^<authentication^>WPA2PSK^</authentication^> >> "%profile_path%"
echo                 ^<encryption^>AES^</encryption^> >> "%profile_path%"
echo                 ^<useOneX^>false^</useOneX^> >> "%profile_path%"
echo             ^</authEncryption^> >> "%profile_path%"
echo             ^<sharedKey^> >> "%profile_path%"
echo                 ^<keyType^>passPhrase^</keyType^> >> "%profile_path%"
echo                 ^<protected^>false^</protected^> >> "%profile_path%"
echo                 ^<keyMaterial^>%2^</keyMaterial^> >> "%profile_path%"
echo             ^</sharedKey^> >> "%profile_path%"
echo         ^</security^> >> "%profile_path%"
echo     ^</MSM^> >> "%profile_path%"
echo ^</WLANProfile^> >> "%profile_path%"
echo Importing Wi-Fi profile...
netsh wlan add profile filename="%profile_path%"
if %errorlevel% neq 0 (
    echo Failed to import Wi-Fi profile.
    pause
    exit /b
)
echo Connecting to Wi-Fi network %1...
netsh wlan connect name="%1"
if %errorlevel% neq 0 (
    echo Failed to connect to Wi-Fi network.
    pause
    exit /b
)
echo Connected to %1 successfully.
timeout /t 3 >nul