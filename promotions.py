from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity) -> float:
        discounted_price = product.price * (1 - self.discount_percentage / 100)
        total_price = discounted_price * quantity
        product.quantity -= quantity
        return total_price


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        total_price = 0.0
        remaining_quantity = quantity
        while remaining_quantity > 0:
            if remaining_quantity >= 2:
                total_price += product.price + product.price * 0.5
                remaining_quantity -= 2
            else:
                total_price += product.price
                remaining_quantity -= 1
        product.quantity -= quantity
        return total_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        total_price = 0.0
        remaining_quantity = quantity
        while remaining_quantity > 0:
            if remaining_quantity >= 3:
                total_price += product.price * 2
                remaining_quantity -= 3
            else:
                total_price += product.price * remaining_quantity
                remaining_quantity = 0
        product.quantity -= quantity
        return total_price

