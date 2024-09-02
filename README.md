# REFi - WindowsRE WiFi Toolset
### by dk865

## Overview
REFi is a toolset designed to facilitate WiFi management within the Windows Recovery Environment (WinRE). It offers various functionalities such as connecting to WiFi networks, managing persistence settings, and launching additional tools.

## Features
- **Do All (Startup Only)**: Configure WiFi settings on startup.
- **Change WiFi Connection**: Switch to a new WiFi network.
- **Enable Network Services**: Activate network drivers.
- **Reload Profile**: Reload the WiFi profile.
- **Persistence Settings**: Add or remove persistence for easier access to tools.
- **WinFile**: Launch WinFile, a file management tool.
- **REstart**: Restart the system.
- **REtask**: Open the task manager.

## Installation
1. Extract the `.zip` file from the releases onto a flash drive, SD card, or hard drive.
2. Boot into WindowsRE using one of the following methods:
   - **From Settings**:
     1. Open **Settings** (press `Win + I`).
     2. Navigate to **Update & Security** (Windows 10) or **System** (Windows 11).
     3. Click on **Recovery**.
     4. Under **Advanced startup**, click **Restart now**. After your PC restarts, select **Troubleshoot** to access WinRE options.
   - **Using the Shift + Restart Option**:
     1. Open the **Start Menu** (press `Win` key).
     2. Hold down the `Shift` key, then click **Restart**. Your PC will restart into WinRE.
   - **From Boot Menu**:
     1. Restart your PC and press `F8`, `F11`, or `Esc` (depending on your computer’s manufacturer) before Windows starts loading.
     2. Select **Troubleshoot** from the boot menu.
   - **Using Installation Media**:
     1. Create a bootable USB or DVD using the Windows Media Creation Tool.
     2. Insert the installation media and restart your PC.
     3. Boot from the media, then select **Repair your computer** to access WinRE.

## Usage
Run the `REFi` application from the extracted files. The GUI provides buttons for each of the functionalities:

- **Do All (Startup Only)**: Opens a window to configure WiFi settings and execute the startup tasks.
- **Change WiFi Connection**: Opens a window to change the WiFi network or connect to a new one.
- **Enable Network Services**: Runs a script to activate network drivers.
- **Reload Profile**: Runs a script to reload the WiFi profile.
- **Persistence Settings**: Opens a window to add or remove persistence, with options for more information.
- **WinFile**: Launches the WinFile tool.
- **REstart**: A Windows Start Replacement for Launching Applications (Don't get your hopes up, it is windowed, but can still launch applications.)
- **REtask**: A Python task manager.
