class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.price}:{self.quantity}"
    
class Cart:
    def __init__(self):
        self.units = []

    def add_unit(self, product, quantity=1):
        self.units.append({"product": product, "quantity": quantity})


    def remove_unit(self, product, quantity=1):
        if product in self.units:
            self.units.remove(product, quantity)

    def calculate_total_price(self):
        total = 0
        for unit in self.units:
            total += unit["product"].price * unit["quantity"]
        return total
    

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_unit(product)
        print(f"{product.name} added to {self.name}'s cart.")


    def remove_from_cart(self, product):
        self.cart.remove_unit(product)
        print(f"{product.name} removed from {self.name}'s cart.")

    def complete_purchase(self):
        total = self.cart.calculate_total_price()
        print(f"{self.name}'s cart total: ${total}$")



product1 = Product("Shirt", 40 , 1)
product2 = Product("Shoes", 80, 1)
product3 = Product("Hat", 15, 1)
product4 = Product("Pants", 70, 1)
product5 = Product("T-shirt", 8 , 1)



customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer1.add_to_cart(product3)
customer1.add_to_cart(product4)
customer1.complete_purchase()
customer1.remove_from_cart(product3)
customer2.remove_from_cart(product3)


customer2.add_to_cart(product5)
customer2.add_to_cart(product2)

customer1.complete_purchase()
customer2.complete_purchase()





