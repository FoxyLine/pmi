from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class File:
    def newFile(self):
        self.filename = "Untitled"
        self.text.delete(0.0, END)

    def saveFile(self):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, "w")
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self):
        f = asksaveasfile(mode="w", defaultextension=".txt")
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title=self.root.t.oops, message=self.root.t.unable_to_save)

    def openFile(self):
        f = askopenfile(mode="r")
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)

    def quit(self):
        entry = askyesno(title=self.root.t.quit, message=self.root.t.sure_exit)
        if entry == True:
            self.root.destroy()
            import sys
            sys.exit(0)

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    filemenu = Menu(menubar, background=root.colors["bg"], foreground=root.colors["fg"])
    objFile = File(text, root)
    filemenu.add_command(label=root.t.new, command=objFile.newFile)
    filemenu.add_command(label=root.t.open_, command=objFile.openFile)
    filemenu.add_command(label=root.t.save, command=objFile.saveFile)
    filemenu.add_command(label=root.t.save_as, command=objFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label=root.t.quit, command=objFile.quit)
    menubar.add_cascade(label=root.t.file, menu=filemenu)
    root.config(menu=menubar)
