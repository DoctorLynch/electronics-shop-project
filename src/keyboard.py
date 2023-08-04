from src.LangMixin import LangMixin
from src.item import Item


class Keyboard(Item, LangMixin):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        return self

    @property
    def language(self):
        return self.__language

