import tkinter as tk
from tkinter import tkk
import subprocess

def run_batch():
    subprocess.run(["path\\to\\your\\batchfile.bat", variable_value])

def dooall_window():
    doall = tk.Toplevel(root)
    doall.title("Do All")

    doall_inf1 = tk.Label(doall, text="This does everything. Only use on startup", font=("Roboto", 24))
    doall_inf1.pack()


root = tk.Tk()

root.title("REFi - WindowsRE WiFi Helper")

title = tk.Label(root, text="REFi - WindowsRE WiFi Helper", font=("Roboto", 24))
madebyme = tk.Label(root, text="by dk865", font=("Roboto", 12), color="teal")

border1 = tk.Label(root, text="-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-", font=("Roboto", 10))
border1.pack()

doall_start = tk.Button(root, text="Do All (Startup Only)", color="Green", font=("Roboto", 12))
doall_start.pack()