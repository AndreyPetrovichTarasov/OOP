import pytest

from src.category import Category
from src.product import Product


def test_invalid_product():

    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_empty_products():

    category_empty = Category("Пустая категория", "Категория без продуктов", [])

    assert category_empty.middle_price() == 0
