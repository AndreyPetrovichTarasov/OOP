from src.product import Product
from src.category import Category


class ProductIterator:
    def __init__(self, obj_category):
        self.category = obj_category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        product_list = self.category.get_product_list()
        if self.index < len(product_list):
            product = product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
