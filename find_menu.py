# import statements
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *

from tkinter import ttk


# creating Edit
class Edit:
    def popup(self, event):
        self.rightClick.post(event.x_root, event.y_root)

    def copy(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel

    def cut(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel
        self.text.delete(SEL_FIRST, SEL_LAST)

    def paste(self, *args):
        self.text.insert(INSERT, self.clipboard)

    def selectAll(self, *args):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(0.0, END)
        self.text.see(INSERT)

    def undo(self, *args):
        self.text.edit_undo()

    def redo(self, *args):
        self.text.edit_redo()

    def find(self, *args):
        self.text.tag_remove("found", "1.0", END)
        target = askstring(self.root.t.find, self.root.t.search_string)

        if target:
            idx = "1.0"
            while 1:
                idx = self.text.search(target, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = "%s+%dc" % (idx, len(target))
                self.text.tag_add("found", idx, lastidx)
                idx = lastidx
            self.text.tag_config("found", foreground="white", background="blue")

    def find(self, *args):
        self.text.tag_remove("found", "1.0", END)
        target = askstring(self.root.t.find, self.root.t.search_string)

        if target:
            idx = "1.0"
            while 1:
                idx = self.text.search(target, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = "%s+%dc" % (idx, len(target))
                self.text.tag_add("found", idx, lastidx)
                idx = lastidx
            self.text.tag_config("found", foreground="white", background="blue")

    def replace(self, *args):
        def test(is_many):
            target = e1.get()
            to_replace = e3.get()
            full_text: str = self.text.get("1.0", END)
            if not is_many:
                full_text = full_text.replace(target, to_replace, 1)
            else:
                full_text = full_text.replace(target, to_replace)
            self.text.delete("1.0", END)
            self.text.insert("1.0", full_text)

        win = Toplevel()
        win.wm_title("Заменить")
        l = ttk.Label(win, text="Фраза")
        l.grid(row=0, column=0)
        e1 = ttk.Entry(win)
        e1.grid(row=0, column=1)
        e2 = ttk.Label(win, text="Заменить на")
        e2.grid(row=0, column=2)
        e3 = ttk.Entry(win)
        e3.grid(row=0, column=3)

        e4 = ttk.Button(
            win,
            text="Заменить",
            command=lambda: test(is_many=False),
        )
        e4.grid(row=1, column=1)
        e4.bind("")
        e5 = ttk.Button(
            win,
            text="Заменить все",
            command=lambda: test(is_many=True),
        )
        e5.grid(row=1, column=2)

    def __init__(self, text, root):
        self.root = root
        self.clipboard = None
        self.text = text
        self.rightClick = Menu(root)


def main(root, text, menubar):
    objEdit = Edit(text, root)
    root.t
    editmenu = Menu(menubar, background=root.colors["bg"], foreground=root.colors["fg"])
    editmenu.add_command(label=root.t.find, command=objEdit.find, accelerator="Ctrl+F")
    editmenu.add_command(
        label=root.t.replace, command=objEdit.replace, accelerator="Ctrl+R"
    )

    menubar.add_cascade(label=root.t.search, menu=editmenu)

    root.bind_all("<Control-z>", objEdit.undo)
    root.bind_all("<Control-y>", objEdit.redo)
    root.bind_all("<Control-f>", objEdit.find)
    root.bind_all("<Control-r>", objEdit.replace)
    root.bind_all("Control-a", objEdit.selectAll)

    objEdit.rightClick.add_command(label="Copy", command=objEdit.copy)
    objEdit.rightClick.add_command(label="Cut", command=objEdit.cut)
    objEdit.rightClick.add_command(label="Paste", command=objEdit.paste)
    objEdit.rightClick.add_separator()
    objEdit.rightClick.add_command(label="Select All", command=objEdit.selectAll)
    objEdit.rightClick.bind("<Control-q>", objEdit.selectAll)

    text.bind("<Button-3>", objEdit.popup)

    root.config(menu=menubar)
