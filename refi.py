import tkinter as tk
import ctypes
import subprocess

def load_font(font_path):
    ctypes.windll.gdi32.AddFontResourceW(font_path)

def winfile():
    subprocess.Popen("assets\\programs\\winfile64.exe")

def restart():
    subprocess.Popen("assets\\programs\\restart.exe")

def retask():
    subprocess.Popen("assets\\programs\\retask.exe")

def doall_window():
    def passyn():
        if wifipassyn.get():
            wifi_pass.config(state="normal")
        else:
            wifi_pass.config(state="disabled")

    def submitcheck():
        wifi_ssid = wifi_name.get()
        wifi_key = wifi_pass.get()
        with open("netname.bat", "w") as file:
            file.write(f"@echo off\nset net={wifi_ssid}\n")

        if wifipassyn.get() == 0:
            subprocess.run(["assets\\connect_nopass.bat", wifi_ssid])
            branch.destroy()
        elif wifipassyn.get() == 1:
            subprocess.run(["assets\\connect_pass.bat", wifi_ssid, wifi_key])
            branch.destroy()

    branch = tk.Toplevel(root)
    branch.title("Do All")
    branch.geometry("500x200")

    doall_inf1 = tk.Label(branch, text="This does everything. Only use on startup", font=("Carter One", 15))
    doall_inf1.pack()

    wifiname_label = tk.Label(branch, text="WiFi Name (SSID)", font=("Carter One", 12))
    wifiname_label.pack()
    
    wifi_name = tk.Entry(branch, width=50)
    wifi_name.pack()
    
    wifipassyn = tk.IntVar()
    passcheckyn = tk.Checkbutton(branch, text="Password?", variable=wifipassyn, command=passyn)
    passcheckyn.pack()
    
    wifi_pass = tk.Entry(branch, width=50, state="disabled")
    wifi_pass.pack()
    
    wifi_submit = tk.Button(branch, text="Submit", command=submitcheck)
    wifi_submit.pack()


def wificonnect_window():
    def passyn():
        if wifipassyn.get():
            wifi_pass.config(state="normal")
        else:
            wifi_pass.config(state="disabled")

    def submitcheck():
        wifi_ssid = wifi_name.get()
        wifi_key = wifi_pass.get()
        with open("netname.bat", "w") as file:
            file.write(f"@echo off\nset net={wifi_ssid}\n")
        if wifipassyn.get() == 0:
            subprocess.run(["assets\\doall_nopass.bat", wifi_ssid])
            branch.destroy()
        elif wifipassyn.get() == 1:
            subprocess.run(["assets\\doall_pass.bat", wifi_ssid, wifi_key])
            branch.destroy()

    branch = tk.Toplevel(root)
    branch.title("Change Wifi")
    branch.geometry("500x200")

    wifi_inf1 = tk.Label(branch, text="Switch or Connect to a New WiFi Network", font=("Carter One", 15))
    wifi_inf1.pack()

    wifiname_label = tk.Label(branch, text="WiFi Name (SSID)", font=("Carter One", 12))
    wifiname_label.pack()
    
    wifi_name = tk.Entry(branch, width=50)
    wifi_name.pack()
    
    wifipassyn = tk.IntVar()
    passcheckyn = tk.Checkbutton(branch, text="Password?", variable=wifipassyn, command=passyn)
    passcheckyn.pack()
    
    wifi_pass = tk.Entry(branch, width=50, state="disabled")
    wifi_pass.pack()
    
    wifi_submit = tk.Button(branch, text="Submit", command=submitcheck)
    wifi_submit.pack()



def pers_window():
    def persinfo_window():
        branch = tk.Toplevel(root)
        branch.title("Persistence Info")
        text_content = (
            "Enabling Persistence makes a copy of these files onto your X: drive so that it is easier to access. This makes it so that when you boot up WindowsRE, type `refi-run` and it will automatically enable your network. You can also just type `refi` to open up the helper, then select load drivers, then reload profile."
        )
        label = tk.Label(branch, text=text_content, font=("Carter One", 15), wraplength=480)
        label.pack()
    def add():
        subprocess.run(["assets\\make_persis.bat"])
        branch.destroy()
    def rem():
        subprocess.run(["assets\\rem_persis.bat"])
        branch.destroy()
    branch = tk.Toplevel(root)
    branch.title("Persistence Settings")
    perstitle = tk.Label(branch, text="Add or Remove Persistence", font=("Carter One", 15))
    perstitle.pack()
    addremfrm = tk.Frame(branch)
    addremfrm.pack()
    addpers = tk.Button(addremfrm, text="Add Persistence", font=("Carter One", 12), fg="red", command=add)
    addpers.pack(side="left")
    rempers = tk.Button(addremfrm, text="Remove Persistenct", font=("Carter One", 12), fg="green", command=rem)
    rempers.pack(side="left")
    pers_infobutton = tk.Button(addremfrm, text="Persistance Info", fg="brown", font=("Carter One", 12), command=persinfo_window)
    pers_infobutton.pack(side="left")

def drivers():
    subprocess.run(["assets\\drivers.bat"])

def reprof():
    subprocess.run(["assets\\reload_profile.bat"])


root = tk.Tk()
root.geometry("725x200")

load_font("assets/CarterOne-Regular.ttf")

root.title("REFi - dk865's WindowsRE WiFi Helper")

title = tk.Label(root, text="REFi - WindowsRE WiFi Helper", font=("Carter One", 15))
title.pack()

madebyme = tk.Label(root, text="by dk865", font=("Carter One", 12), fg="teal")
madebyme.pack()

buttonfrm = tk.Frame(root)
buttonfrm.pack()
doall_start = tk.Button(buttonfrm, text="Do All (Startup Only)", fg="orange", font=("Carter One", 12), command=doall_window)
doall_start.pack(side="left")
drivers_start = tk.Button(buttonfrm, text="Enable Network Services", fg="green", font=("Carter One", 12), command=drivers)
drivers_start.pack(side="left")
change_start = tk.Button(buttonfrm, text="Change WiFi Connection", fg="blue", font=("Carter One", 12), command=wificonnect_window)
change_start.pack(side="left")
reprof_start = tk.Button(buttonfrm, text="Reload Profile", fg="brown", font=("Carter One", 12), command=reprof)
reprof_start.pack(side="left")

extras_label = tk.Label(root, text = "Extras", font=("Carter One", 15))
extras_label.pack()

extras = tk.Frame(root)
extras.pack()
pers_startbutton = tk.Button(extras, text="Persistance Settings", fg="red", font=("Carter One", 12), command=pers_window)
pers_startbutton.pack(side="left")
winfile_startbutton = tk.Button(extras, text="WinFile", fg="purple", font=("Carter One", 12), command=winfile)
winfile_startbutton.pack(side="left")
restart_startbutton = tk.Button(extras, text="REstart", fg="maroon", font=("Carter One", 12), command=restart)
restart_startbutton.pack(side="left")
restask_startbutton = tk.Button(extras, text="REtask", fg="brown", font=("Carter One", 12), command=retask)
restask_startbutton.pack(side="left")

root.mainloop()
