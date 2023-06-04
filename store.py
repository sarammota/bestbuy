import products


class Store:
    def __init__(self, product_list):
        self.store = product_list

    def add_product(self, product):
        self.store.append(product)
        return self.store

    def remove_product(self, product):
        self.store.remove(product)
        return self.store

    def get_total_quantity(self) -> int:
        total_quantity = sum(
            product.get_quantity() for product in self.store if not isinstance(product, products.NonStockedProduct))
        return total_quantity

    def get_all_products(self) -> [products.Product]:
        return [product for product in self.store if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

