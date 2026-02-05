from product import Product


class Order:

    def __init__(self):
        self.__products = []
        self.__total_amount = 0.0

    @property
    def products(self):
        return self.__products.copy()

    @property
    def total_amount(self):
        return self.__total_amount

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ValueError("Must be a Product instance!")
        self.__products.append(product)
        self.calculate_total()

    def calculate_total(self):
        total = 0
        for product in self.__products:
            total += product.price * product.quantity
        self.__total_amount = total
        return self.__total_amount

    def __str__(self):
        return f"Order(products={len(self.__products)}, total=${self.__total_amount:.2f})"
