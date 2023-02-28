# import statements
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu
import tkinter as tk
import find_menu
from tkinter import ttk
import datetime
import configparser
from trans import Trans
import sys

from pygments.lexers import PythonLexer, ErlangLexer, TypeScriptLexer
from pygments.token import Token



def run():
    config = configparser.ConfigParser()
    config.read("settings.ini")

    lexer = {"erlang": ErlangLexer(), "python": PythonLexer(), "js": TypeScriptLexer()}[
        config["settings"]["syntax"]
    ]

    theme = config["settings"]["theme"]

    token_type_to_tag = {
        Token.Keyword: "keyword",
        Token.Name.Variable: "operator",
        Token.Operator.Word: "keyword",
        Token.Name.Builtin: "keyword",
        Token.Literal.String.Single: "string_literal",
        Token.Literal.String.Double: "string_literal",
        Token.Keyword.Declaration: "keyword",
        Token.Operator: "operator",
        Token.Name.Other: "string_literal_other",
        Token.Name.Namespace: "keyword",
        Token.Comment: "comment",
    }

    colors = {
        "default": {
            "fg": "#000000",
            "bg": "white",
            "status_bar": "white",
            "keyword": "blue",
            "string_literal": "red",
            "string_literal_other": "#BF9000",
            "operator": "#00b300",
            "comment": "red",
        },
        "grey": {
            "bg": "#343434",
            "fg": "white",
            "status_bar": "#0D0D0D",
            "font_color": "white",
            "keyword": "#3D83D6",
            "string_literal": "#C95F5F",
            "string_literal_other": "#FFF500",
            "operator": "#51AE51",
            "comment": "#808080",
        },
        "clown": {
            "bg": "#190D2C",
            "status_bar": "#469A58",
            "fg": "white",
            "keyword": "#0075FF",
            "string_literal": "#FF5925",
            "string_literal_other": "#FFF500",
            "operator": "#00FF00",
            "comment": "#626262",
        },
    }[theme]


    def on_edit(text, event=None):
        for tag in text.tag_names():
            text.tag_remove(tag, 1.0, tk.END)
        s = text.get(1.0, tk.END)
        tokens = lexer.get_tokens_unprocessed(s)

        for i, token_type, token in tokens:
            j = i + len(token)
            if token_type in token_type_to_tag:
                text.tag_add(
                    token_type_to_tag[token_type],
                    get_text_coord(s, i),
                    get_text_coord(s, j),
                )

        text.edit_modified(0)


    def get_text_coord(s: str, i: int):
        for row_number, line in enumerate(s.splitlines(keepends=True), 1):
            if i < len(line):
                return f"{row_number}.{i}"

            i -= len(line)



    root = Tk()

    def change_lang(lang):
        root.destroy()
        config.set("settings", "lang", lang)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

        root.update()

    def change_syntax(sntx):
        root.destroy()
        config.set("settings", "syntax", sntx)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

    def change_theme(theme):
        root.destroy()
        config.set("settings", "theme", theme)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)

    root.config_ini = config
    root.change_lang = change_lang
    root.change_syntax = change_syntax
    root.change_theme = change_theme
    root.colors = colors
    root.t = Trans(config["settings"]["lang"])
    root.title("TextEditor-newfile")
    root.geometry("300x250+300+300")
    root.minsize(width=400, height=400)
    root.configure(bg="#FFFFFF")
    statusbar_var = StringVar()
    statusbar = ttk.Label(
        root, textvariable=statusbar_var, relief=tk.SUNKEN, anchor=tk.W, background=colors["status_bar"], foreground=colors["fg"]
    )
    # Text(f)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)
    text = ScrolledText(
        root,
        state="normal",
        bg=colors["bg"],
        foreground=colors["fg"],
        height=400,
        width=400,
        wrap="word",
        pady=2,
        padx=3,
        undo=True,
    )
    text.pack(fill=Y, expand=1)
    text.bind("<<Modified>>", lambda e: on_edit(text))

    text.tag_config("keyword", foreground=colors["keyword"])
    text.tag_config("string_literal", foreground=colors["string_literal"])
    text.tag_config("string_literal_other", foreground=colors["string_literal_other"])
    text.tag_config("operator", foreground=colors["operator"])
    text.tag_config("comment", foreground=colors["comment"])

    def change_status_bar(e):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row, col = e.widget.index(INSERT).split(".")
        statusbar_var.set(f"Строка {row}. Время {time}")

    def updater():
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row, col = text.index(INSERT).split(".")
        statusbar_var.set(f"Строка {row}. Время {time}")
        root.after(1000, updater)

    text.focus_set()
    text.bind("<KeyPress>", func=change_status_bar)
    menubar = Menu(root)
    style = ttk.Style(root)

    file_menu.main(root, text, menubar)
    edit_menu.main(root, text, menubar)
    find_menu.main(root, text, menubar)
    format_menu.main(root, text, menubar, style)
    help_menu.main(root, text, menubar)

    updater()
    root.protocol("WM_DELETE_WINDOW", lambda: sys.exit(1))
    root.mainloop()


while True:
    run()
