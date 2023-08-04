import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5, 'EN')


class TestKeyboard:

    def test_init_keyboard(self, keyboard):
        assert keyboard.name == 'Dark Project KD87A'
        assert keyboard.price == 9600
        assert keyboard.quantity == 5
        assert keyboard.language == 'EN'


