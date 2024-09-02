import tkinter as tk
from tkinter import ttk
import os

class Restart(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("REstart by dk865")
        self.geometry("800x600")

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("Path"), show="tree")
        self.tree.heading("#0", text="Shortcut Name")
        self.tree.heading("Path", text="Path")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.load_start_menu()

    def load_start_menu(self):
        user_start_menu = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
        all_users_start_menu = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs")

        self.insert_programs(user_start_menu, "")
        self.insert_programs(all_users_start_menu, "")

    def insert_programs(self, directory, parent_id):
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isdir(path):
                folder_id = self.tree.insert(parent_id, "end", text=item, open=True, tags=("folder",))
                self.insert_programs(path, folder_id)
            else:
                if path.lower().endswith(".lnk"):
                    self.tree.insert(parent_id, "end", text=item, values=(path,), tags=("file",))

        self.tree.tag_configure("folder", background="#e0f0ff")
        self.tree.tag_configure("file", foreground="#006400")

if __name__ == "__main__":
    app = Restart()
    app.mainloop()
