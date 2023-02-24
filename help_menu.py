# import statements
from tkinter import *
from tkinter.messagebox import *


message = """
Некоторые горячие клавиши

CTRL + R - Заменить
CTRL + F - Найти
CTRL + C - Скопировать выделенный текст
CTRL + V - Вставить скопированный текст
CTRL + X - Вырезать выделенный текст
CTRL + A - Выделить весь текст
CTRL + Z - Отмена действия
"""


class Help:
    def help_(self, root):
        showinfo(
            title=root.t.help,
            message=root.t.desc,
        )

    def about(self, root):
        showinfo(
            title=root.t.about,
            message="Текстовый редактор 1.0\n© Правая палочка Твикс (ФГБОУ ВО «МАГУ»), 2023.",
        )


def main(root, text, menubar):
    help = Help()

    helpMenu = Menu(menubar, background=root.colors["bg"], foreground=root.colors["fg"])
    helpMenu.add_command(label=root.t.help, command=lambda: help.help_(root))
    helpMenu.add_command(label=root.t.about, command=lambda: help.about(root))
    menubar.add_cascade(label=root.t.help, menu=helpMenu)

    root.config(menu=menubar)
