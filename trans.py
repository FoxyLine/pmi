from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *


desc_ru = """
Некоторые горячие клавиши

CTRL + R - Заменить
CTRL + F - Найти
CTRL + C - Скопировать выделенный текст
CTRL + V - Вставить скопированный текст
CTRL + X - Вырезать выделенный текст
CTRL + A - Выделить весь текст
CTRL + Z - Отмена действия
"""


desc_eng = """
Hot-keys

CTRL + R - Replace
CTRL + F - Find
CTRL + C - Copy the selected text
CTRL + V - Paste copied text
CTRL + X - Cut selected text
CTRL + A - Highlight all text
CTRL + Z - Cancel action
"""


class Trans:
    def __init__(self, lang) -> None:
        self.lang = lang

    @property
    def find(self):
        return "Поиск:" if self.lang == "ru" else "Find:"

    @property
    def search_string(self):
        return "Поиск строки" if self.lang == "ru" else "Search String"

    @property
    def replace(self):
        return "Замена" if self.lang == "ru" else "Replace"

    @property
    def phrase(self):
        return "Фраза" if self.lang == "ru" else "Phrase:"

    @property
    def replace_on(self):
        return "Заменить на" if self.lang == "ru" else "Replace"

    @property
    def replace_all(self):
        return "Заменить все" if self.lang == "ru" else "Replace all"

    @property
    def copy(self):
        return "Копировать" if self.lang == "ru" else "Copy"

    @property
    def cut(self):
        return "Вырезать" if self.lang == "ru" else "Cut"

    @property
    def paste(self):
        return "Вставить" if self.lang == "ru" else "Paste"

    @property
    def redo(self):
        return "Вернуть" if self.lang == "ru" else "Redo"

    @property
    def undo(self):
        return "Отменить" if self.lang == "ru" else "Undo"

    @property
    def find(self):
        return "Найти" if self.lang == "ru" else "Find"

    @property
    def select_all(self):
        return "Выделить все" if self.lang == "ru" else "Select all"

    @property
    def edit(self):
        return "Редактировать" if self.lang == "ru" else "Edit"

    @property
    def new(self):
        return "Новый" if self.lang == "ru" else "New"

    @property
    def open_(self):
        return "Открыть" if self.lang == "ru" else "Open"

    @property
    def save(self):
        return "Сохранить" if self.lang == "ru" else "Save"

    @property
    def save_as(self):
        return "Сохранить как..." if self.lang == "ru" else "Save as..."

    @property
    def quit(self):
        return "Выйти" if self.lang == "ru" else "Exit"

    @property
    def file(self):
        return "Файл" if self.lang == "ru" else "File"

    @property
    def oops(self):
        return "Ой!" if self.lang == "ru" else "Oops..."

    @property
    def unable_to_save(self):
        return "Невозможно сохранить файл" if self.lang == "ru" else "Unable to save file"

    @property
    def sure_exit(self):
        return (
            "Вы точно хотите выйти?"
            if self.lang == "ru"
            else "Are you sure you want to quit?"
        )

    @property
    def search(self):
        return "Поиск" if self.lang == "ru" else "Search"

    @property
    def theme(self):
        return "Тема" if self.lang == "ru" else "Theme"

    @property
    def font(self):
        return "Шрифт" if self.lang == "ru" else "Font"

    @property
    def view(self):
        return "Вид" if self.lang == "ru" else "View"

    @property
    def view(self):
        return "Вид" if self.lang == "ru" else "View"

    @property
    def help(self):
        return "Помощь" if self.lang == "ru" else "Help"

    @property
    def about(self):
        return "О программе" if self.lang == "ru" else "About"

    @property
    def desc(self):
        return desc_ru if self.lang == "ru" else desc_eng

    @property
    def sntx(self):
        return "Подсветка синтакиса" if self.lang == "ru" else "Syntax HightLight"
