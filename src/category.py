from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_product_list(self):
        return self.__products

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    # @add_product.setter
    # def add_product(self, product: Product):
    #     self.__products.append(product)
    #     Category.product_count += 1

    def middle_price(self):
        try:
            return sum([product.quantity for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
