# import statements
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *
import time
from tkinter import ttk


class Format:
    def __init__(self, text, root):
        self.root = root
        self.text = text

    def changeBg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(bg=hexstr)

    def changeFg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(fg=hexstr)

    def bold(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except:
            pass

    def italic(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass

    def underline(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass

    def overstrike(self, *args):
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass

    def set_eng(self):
        self.root.change_lang("eng")

    def set_ru(self):
        self.root.change_lang("ru")

    def addDate(self):
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + "/" + month + "/" + year
        self.text.insert(INSERT, date, "a")


def main(root, text, menubar, style=None):
    objFormat = Format(text, root)

    fontoptions = families(root)
    font = Font(family="Arial", size=10)
    text.configure(font=font)

    formatMenu = Menu(menubar, background=root.colors["bg"], foreground=root.colors["fg"])

    fsubmenu = Menu(formatMenu, tearoff=0, background=root.colors["bg"], foreground=root.colors["fg"])
    ssubmenu = Menu(formatMenu, tearoff=0, background=root.colors["bg"], foreground=root.colors["fg"])
    # themesubmenu = Menu(formatMenu, tearoff=0)
    sntxsubmenu = Menu(formatMenu, tearoff=0, background=root.colors["bg"], foreground=root.colors["fg"])
    themesubmenu = Menu(formatMenu, tearoff=0, background=root.colors["bg"], foreground=root.colors["fg"])

    for option in fontoptions:
        fsubmenu.add_command(
            label=option, command=lambda option=option: font.configure(family=option)
        )
    for value in range(1, 31):
        ssubmenu.add_command(
            label=str(value), command=lambda value=value: font.configure(size=value)
        )

    for theme in ["default", "grey", "clown"]:
        themesubmenu.add_command(
            label=theme, command=lambda value=theme: root.change_theme(value)
        )

    def temp(theme):
        style.theme_use(theme)

    # for theme in style.theme_names():
    #     themesubmenu.add_command(
    #         label=str(theme), command=lambda value=theme: temp(value)
    #     )

    for sntx in ["erlang", "python", "js"]:
        sntxsubmenu.add_command(
            label=str(sntx), command=lambda value=sntx: root.change_syntax(value)
        )

    formatMenu.add_cascade(label=root.t.font, underline=0, menu=fsubmenu)
    formatMenu.add_cascade(label=root.t.theme, underline=0, menu=themesubmenu)
    formatMenu.add_cascade(label=root.t.sntx, underline=0, menu=sntxsubmenu)
    formatMenu.add_command(label="english", command=objFormat.set_eng)
    formatMenu.add_command(label="Русский", command=objFormat.set_ru)

    menubar.add_cascade(label=root.t.view, menu=formatMenu)

    root.bind_all("<Control-b>", objFormat.bold)
    root.bind_all("<Control-i>", objFormat.italic)
    root.bind_all("<Control-u>", objFormat.underline)
    root.bind_all("<Control-T>", objFormat.overstrike)

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.config(menu=menubar)


if __name__ == "__main":
    print("Please run 'main.py'")
