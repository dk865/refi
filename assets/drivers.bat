@echo off
echo Initializing network services...
wpeutil initializenetwork
net start wlansvc
if %errorlevel% neq 0 (
    echo Failed to initialize network services.
    pause
    exit /b
)
echo Installing Wi-Fi Driver...
pnputil /add-driver drivers/netwtw08.inf /install
echo Done (:
timeout /t 3 >nul
exit