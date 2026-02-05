from customer import Customer
from order import Order
from product import Product


class Shop:
    def __init__(self):
        self.products = {}
        self.customers = {}

    def load_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        mode = None  # file section

        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                if line == '# PRODUCTS':
                    mode = 'Products'
                elif line == '# CUSTOMERS':
                    mode = 'Customers'
                elif line == '# ORDERS':
                    mode = 'Orders'
                continue

            if mode == 'Products':
                name, price, quantity = line.split(',')
                product = Product(name, float(price), int(quantity))
                self.products[name] = product

            elif mode == 'Customers':
                name, email = line.split(',')
                customer = Customer(name, email)
                self.customers[email] = customer

            elif mode == 'Orders':
                email, product_name, quantity = line.split(',')

                if email not in self.customers:
                    print(f"Customer {email} not found")
                    continue

                if product_name not in self.products:
                    print(f"Product {product_name} not found")
                    continue

                customer = self.customers[email]

                order = Order()
                product = Product(
                    product_name,
                    self.products[product_name].price,
                    int(quantity)
                )
                order.add_product(product)
                customer.add_order(order)

    def print_shop_info(self):
        print("=== SHOP INFORMATION ===\n")

        print(f"Products in stock: {len(self.products)}")
        for product in self.products.values():
            print(f"{product}")

        print(f"\nCustomers: {len(self.customers)}")
        for customer in self.customers.values():
            print(f"\n{customer}")
            for i, order in enumerate(customer.orders, 1):
                print(f"  Order {i}: ${order.total_amount:.2f}")
