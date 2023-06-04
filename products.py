import promotions
import promotions

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
        self.promotion = None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def activate(self):
        return self.quantity >= 0

    def deactivate(self):
        return not self.activate()

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promotion_info = self.promotion.__class__.__name__ if self.promotion else "None"
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promotion_info}"

    def buy(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        elif quantity <= 0:
            raise Exception("Invalid purchase amount.")
        elif quantity > self.quantity:
            raise Exception("Insufficient quantity available.")

        total_price = quantity * self.price
        self.quantity -= quantity

        return total_price

   # def show(self) -> str:
   #    return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=float('inf'))

    def show(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity=0, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise Exception("Invalid purchase amount.")
        elif quantity > self.maximum:
            raise Exception("Exceeded maximum quantity per purchase.")

        total_price = quantity * self.price
        self.quantity -= quantity  # Deduct the purchased quantity from the total stock
        print(f"The total amount is ${total_price} for {quantity} {self.name}.")
        return total_price
