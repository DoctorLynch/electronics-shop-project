from src.LangMixin import LangMixin
from src.item import Item


class Keyboard(Item, LangMixin):
    def __init__(self, name, price, quantity,):
        super().__init__(name, price, quantity)
        LangMixin.__init__(self)

