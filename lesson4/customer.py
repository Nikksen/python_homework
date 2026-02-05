from order import Order


class Customer:

    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email
        self.__orders = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty!")
        self.__name = name.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if not email or '@' not in email:
            raise ValueError("Invalid email!")
        self.__email = email

    @property
    def orders(self):
        return self.__orders.copy()

    def add_order(self, order: Order):
        if not isinstance(order, Order):
            raise ValueError("Must be an Order instance!")
        self.__orders.append(order)

    def get_orders_count(self):
        return len(self.__orders)

    def get_total_spent(self):
        total = 0
        for order in self.__orders:
            total += order.total_amount
        return total

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, orders={len(self.__orders)}, total_spent=${self.get_total_spent():.2f})"
