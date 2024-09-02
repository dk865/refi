@echo off
REM Enable Networking
echo Initializing network services...
wpeutil initializenetwork
net start wlansvc
if %errorlevel% neq 0 (
    echo Failed to initialize network services.
    pause
    exit /b
)
echo Installing Wi-Fi Driver...
pnputil /add-driver 10-11/netwtw08.inf /install

REM Ask for Wi-Fi details
set /p ssid="Enter your Wi-Fi SSID: "
set /p password="Enter your Wi-Fi password: "

REM Create Wi-Fi Profile XML file
set profile_path=%~dp0wifi-profile.xml
echo Creating Wi-Fi profile XML file...
echo ^<?xml version="1.0"?^> > "%profile_path%"
echo ^<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"^> >> "%profile_path%"
echo     ^<name^>%ssid%^</name^> >> "%profile_path%"
echo     ^<SSIDConfig^> >> "%profile_path%"
echo         ^<SSID^> >> "%profile_path%"
echo             ^<name^>%ssid%^</name^> >> "%profile_path%"
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
echo                 ^<keyMaterial^>%password%^</keyMaterial^> >> "%profile_path%"
echo             ^</sharedKey^> >> "%profile_path%"
echo         ^</security^> >> "%profile_path%"
echo     ^</MSM^> >> "%profile_path%"
echo ^</WLANProfile^> >> "%profile_path%"

REM Import the Wi-Fi Profile
echo Importing Wi-Fi profile...
netsh wlan add profile filename="%profile_path%"
if %errorlevel% neq 0 (
    echo Failed to import Wi-Fi profile.
    pause
    exit /b
)

REM Connect to Wi-Fi
echo Connecting to Wi-Fi network %ssid%...
netsh wlan connect name="%ssid%"
if %errorlevel% neq 0 (
    echo Failed to connect to Wi-Fi network.
    pause
    exit /b
)

echo Connected to %ssid% successfully.
pause
