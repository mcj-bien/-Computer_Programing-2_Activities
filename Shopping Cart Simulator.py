# Shopping Cart Simulator
# Created by: Jabien

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = price
        print(item, "has been added to the cart.")

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
            print(item, "has been removed from the cart.")
        else:
            print("Item not found in the cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for item, price in self.cart.items():
                print(item, "- ₱", price)
                total += price
            print("Total: ₱", total)

    def checkout(self):
        if len(self.cart) == 0:
            print("Your cart is empty. Nothing to checkout.")
        else:
            total = sum(self.cart.values())
            print("\nCheckout Complete!")
            print("Total amount to pay: ₱", total)
            print("Thank you for shopping!")
            self.cart.clear()


print("Welcome to Jabien's Shopping Cart Simulator")

cart = ShoppingCart()

while True:
    print("\nMenu")
    print("1 - Add Item")
    print("2 - Remove Item")
    print("3 - View Cart")
    print("4 - Checkout")
    print("5 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price (₱): "))
        cart.add_item(item, price)

    elif choice == "2":
        item = input("Enter item name to remove: ")
        cart.remove_item(item)

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        print("Goodbye! Thank you for using Jabien's Shopping Cart.")
        break

    else:
        print("Invalid choice. Please try again.")