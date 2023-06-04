import products
import promotions
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice()
third_one_free = promotions.ThirdOneFree()
thirty_percent = promotions.PercentDiscount(discount_percentage=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)  # Assign promotion to the first product
product_list[1].set_promotion(third_one_free)     # Assign promotion to the second product
product_list[2].set_promotion(thirty_percent)     # Assign promotion to the third product

def start(store):
    print("Store Menu")
    print("__________")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    choice = input("Please choose a number: ")

    if choice == "1":
        print("------")
        for index, product in enumerate(store.get_all_products(), start=1):
            promotion_info = type(product.get_promotion()).__name__ if product.get_promotion() else "None"
            if promotion_info == "SecondHalfPrice":
                promotion_info = "Second Half price!"
            elif promotion_info == "ThirdOneFree":
                promotion_info = "Third One Free!!"
            elif promotion_info == "PercentDiscount":
                promotion_info = "30% off!!!"
            print(
                f"{index}. {product.name}, Price: ${product.price}, Quantity: "
                f"{product.quantity}, Promotion: {promotion_info}"
            )

    elif choice == "2":
        total_quantity = store.get_total_quantity()
        print(f"Total quantity in store: {total_quantity}")


    elif choice == "3":

        product_name = input("Name of the product: ").lower()
        product_quantity = int(input("Quantity of product: "))
        found_product = None

        for product in store.get_all_products():
            if product_name in product.name.lower():
                found_product = product
                break

        if found_product is None:
            print("Product not found in store.")
        else:
            try:
                order_total = found_product.buy(product_quantity)
                print(f"The order of {product_quantity} {found_product.name} is a total of ${order_total}")

            except Exception as e:
                print(f"Failed to place the order: {str(e)}")

    elif choice == "4":
        print("Thank you for using the store. Goodbye!")
        quit()

    else:
        print("Invalid choice. Please try again.")

while True:
    start(store.Store(product_list))