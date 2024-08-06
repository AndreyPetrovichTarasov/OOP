import pytest

from src.product import Product
from src.category import Category


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство"
    assert category.products == ""

    assert category.product_count == 0
    assert category.category_count == 1


def test_add_product():
    # Arrange
    category = Category("Electronics", "Various electronic products", [])
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    category.add_product(product)

    assert category.product_count == 1
    assert category.products == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'


def test_products_property():
    category = Category("Electronics", "Various electronic products", [])
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 14", "128GB, Black", 150000.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    products_str = category.products

    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "iPhone 14, 150000.0 руб. Остаток: 3 шт." in products_str


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 0 шт."


def test_add_product_error():
    # Arrange
    category = Category("Electronics", "Various electronic products", [])
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    with pytest.raises(TypeError):
        category.add_product(category)
