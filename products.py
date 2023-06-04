class Product:
    def __init__(self, name=str, price=float, quantity=int):
        if price <= 0:
            raise Exception("Invalid price.")
        elif quantity <= 0:
            raise Exception("Invalid quantity.")
        elif name == "":
            raise Exception("Invalid name.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def activate(self):
        return self.quantity > 0

    def deactivate(self):
        return not self.activate()

    def show(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:

        if quantity <= 0:
            raise Exception("Invalid purchase amount.")
        elif quantity > self.quantity:
            raise Exception("Insufficient quantity available.")

        total_price = quantity * self.price
        print(f"The total amount is ${total_price} for {quantity} {self.name}.")
        remaining_quantity = self.quantity - quantity
        self.quantity = remaining_quantity
        print (f"There are {self.quantity} {self.name} units remaining.")

        return total_price
