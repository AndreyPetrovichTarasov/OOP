import json
from pathlib import Path

from src.product import Product
from src.category import Category
from data.config_path import json_path

ROOT_Path = Path(__file__).resolve().parent.parent


def read_json(path: str) -> dict:
    """Чтение файла json"""
    with open(Path(ROOT_Path,json_path), "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_objects_from_json(data):
    """Преобразование элементов списка словарей в объекты класса Product, Category"""
    categories = []
    for category in list_products:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


list_products = read_json(json_path)
list_categories = create_objects_from_json(list_products)
