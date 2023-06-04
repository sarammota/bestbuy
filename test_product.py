import pytest
import products


def test_create_normal_product():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert isinstance(product, products.Product)


def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        products.Product("", price=-10, quantity=50)


def test_product_becomes_inactive_at_0_quantity():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    quantity = 5
    total_price = product.buy(quantity)
    assert product.get_quantity() == 95
    assert total_price == quantity * product.price


def test_buying_larger_quantity_than_exists_raises_exception():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    quantity = 150
    with pytest.raises(Exception):
        product.buy(quantity)


