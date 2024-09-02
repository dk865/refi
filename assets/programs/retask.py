import tkinter as tk
from tkinter import ttk, messagebox
import psutil

class RETask:
    def __init__(self, root):
        self.root = root
        self.root.title("REtask")

        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("PID", "Name"), show='headings')
        self.tree.heading("PID", text="PID")
        self.tree.heading("Name", text="Name")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh)
        self.refresh_button.pack(pady=5)

        self.end_task_button = tk.Button(root, text="End Task", command=self.end_task)
        self.end_task_button.pack(pady=5)

        self.refresh()

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for proc in psutil.process_iter(['pid', 'name']):
            self.tree.insert("", tk.END, values=(proc.info['pid'], proc.info['name']))

    def end_task(self):
        try:
            selected_item = self.tree.selection()[0]
            pid = int(self.tree.item(selected_item, 'values')[0])
            proc = psutil.Process(pid)
            proc.terminate()
            self.refresh()
        except IndexError:
            messagebox.showwarning("Warning", "No process selected")
        except psutil.NoSuchProcess:
            messagebox.showwarning("Warning", "Process not found or already terminated")
        except psutil.AccessDenied:
            messagebox.showwarning("Warning", "Access denied to terminate process")

if __name__ == "__main__":
    root = tk.Tk()
    app = RETask(root)
    root.mainloop()
