class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.__product_name = name
        self.__product_price = price
        self.__product_quantity = quantity

    @property
    def price(self):
        return self.__product_price

    @price.setter
    def price(self, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative!")
        self.__product_price = price

    @property
    def quantity(self):
        return self.__product_quantity

    @quantity.setter
    def quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")
        self.__product_quantity = quantity

    @property
    def name(self):
        return self.__product_name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Name cannot be empty!")
        self.__product_name = name
