import tkinter as tk
import ctypes
import subprocess

def load_font(font_path):
    ctypes.windll.gdi32.AddFontResourceW(font_path)

def doall_window():

    def passyn():
        if wifipassyn.get():
            wifi_pass.config(state="normal")
        else:
            wifi_pass.config(state="disabled")

    def submitcheck():
        wifi_ssid = wifi_name.get()
        wifi_key = wifi_pass.get()
        if wifipassyn.get() == 0:
            subprocess.run(["assets\\connect_nopass.bat", wifi_ssid])
            doall.destroy()
        elif wifipassyn.get() == 1:
            subprocess.run(["assets\\connect_pass.bat", wifi_ssid, wifi_key])
            doall.destroy()

    doall = tk.Toplevel(root)
    doall.title("Do All")
    doall.geometry("500x200")

    doall_inf1 = tk.Label(doall, text="This does everything. Only use on startup", font=("Carter One", 15))
    doall_inf1.pack()

    wifiname_label = tk.Label(doall, text="WiFi Name (SSID)", font=("Carter One", 12))
    wifiname_label.pack()
    
    wifi_name = tk.Entry(doall, width=50)
    wifi_name.pack()
    
    wifipassyn = tk.IntVar()
    passcheckyn = tk.Checkbutton(doall, text="Password?", variable=wifipassyn, command=passyn)
    passcheckyn.pack()
    
    wifi_pass = tk.Entry(doall, width=50, state="disabled")
    wifi_pass.pack()
    
    wifi_submit = tk.Button(doall, text="Submit", command=submitcheck)
    wifi_submit.pack()

root = tk.Tk()
root.geometry("500x200")

load_font("assets/CarterOne-Regular.ttf")

root.title("REFi - dk865's WindowsRE WiFi Helper")

title = tk.Label(root, text="REFi - WindowsRE WiFi Helper", font=("Carter One", 15))
title.pack()

madebyme = tk.Label(root, text="by dk865", font=("Carter One", 12), fg="teal")
madebyme.pack()

buttonfrm = tk.Frame(root)
buttonfrm.pack()
doall_start = tk.Button(buttonfrm, text="Do All (Startup Only)", fg="blue", font=("Carter One", 12), command=doall_window)
doall_start.pack()

root.mainloop()
