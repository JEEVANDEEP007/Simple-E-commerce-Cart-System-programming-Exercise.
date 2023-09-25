from abc import ABC, abstractmethod

# Product classes with attributes like name, price, and availability status
class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

class Laptop(Product):
    pass

class Headphones(Product):
    pass

# Discount Strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

# Concrete discount strategies
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total * (1 - self.percentage / 100)

class BuyOneGetOneFree(DiscountStrategy):
    def apply_discount(self, total):
        return total

# Cart item representation
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

# Shopping cart with add, update, remove, and checkout functionality
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def update_quantity(self, product, quantity):
        for item in self.items:
            if item.product == product:
                item.quantity = quantity
                return

    def remove_item(self, product):
        self.items = [item for item in self.items if item.product != product]

    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.items)
        return total

    def checkout(self, discount_strategy=None):
        total = self.calculate_total()
        if discount_strategy:
            total = discount_strategy.apply_discount(total)
        return total

# Sample product data
laptop1 = Laptop("Laptop", 1000)
headphones1 = Headphones("Headphones", 50)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_item(laptop1, quantity=2)
cart.add_item(headphones1, quantity=1)

# Calculate and display the total bill
total_bill = cart.checkout(PercentageDiscount(10))  # Apply a 10% discount
print(f"Cart Items: You have {cart.items[0].quantity} {cart.items[0].product.name}s and {cart.items[1].quantity} {cart.items[1].product.name} in your cart.")
print(f"Total Bill: Your total bill is ${total_bill:.2f}")
