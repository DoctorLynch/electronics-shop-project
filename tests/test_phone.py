import pytest

from src.phone import Phone

@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120000, 5, 2)


class TestPhone:

    def test_init_phone(self, phone):
        assert phone.price == 120000
        assert phone.name == "iPhone 14"
        assert phone.quantity == 5
        assert phone.number_of_sim == 2

    def test_repr_phone(self, phone):
        assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
        assert str(phone) == 'iPhone 14'


