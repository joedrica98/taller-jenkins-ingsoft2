import pytest
from main import Meal, Order


def test_meal_init():
    meal = Meal("Pasta", 10, "Regular")
    assert meal.name == "Pasta"
    assert meal.price == 10
    assert meal.category == "Regular"


def test_order_init():
    order = Order()
    assert order.meals == {}


def test_add_meal():
    order = Order()
    meal = Meal("Pasta", 10, "Regular")
    order.add_meal(meal, 5)
    assert meal.name in order.meals
    assert order.meals[meal.name][1] == 5


def test_add_meal_zero_quantity():
    order = Order()
    meal = Meal("Pasta", 10, "Regular")
    order.add_meal(meal, 0)
    assert meal.name not in order.meals


def test_get_total_no_discount():
    order = Order()
    meal = Meal("Pasta", 10, "Regular")
    order.add_meal(meal, 3)
    assert order.get_total() == 30


def test_get_total_quantity_discount():
    order = Order()
    meal = Meal("Pasta", 10, "Regular")
    order.add_meal(meal, 6)
    assert order.get_total() == 54  # 10*6*0.9


def test_get_total_special_meal_additional_fee():
    order = Order()
    meal = Meal("Chef's Special Steak", 25, "Special")
    order.add_meal(meal, 2)
    assert order.get_total() == 52.5  # 25*2 + 25*2*0.05


def test_get_total_multiple_discounts():
    order = Order()
    regular_meal = Meal("Pasta", 10, "Regular")
    special_meal = Meal("Chef's Special Steak", 25, "Special")
    order.add_meal(regular_meal, 6)
    order.add_meal(special_meal, 6)
    # (10*6*0.8 + 25*6 + 25*6*0.05) - 25
    assert order.get_total() == 138  # After applying all discounts and fees
