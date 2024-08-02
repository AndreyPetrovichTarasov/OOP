import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def product2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство",
        []
    )
