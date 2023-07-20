class Meal:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Order:
    def __init__(self):
        self.meals = {}

    def add_meal(self, meal, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
        if meal.name in self.meals:
            self.meals[meal.name][1] += quantity
        else:
            self.meals[meal.name] = [meal, quantity]

    def get_total(self):
        total = 0
        total_meals = 0
        special_meal_total = 0
        for meal, quantity in self.meals.values():
            total += meal.price * quantity
            total_meals += quantity
            if meal.category == 'Special':
                special_meal_total += meal.price * quantity
        if total_meals > 10:
            total *= 0.8
        elif total_meals > 5:
            total *= 0.9
        if total > 100:
            total -= 25
        elif total > 50:
            total -= 10
        total += special_meal_total * 0.05
        return total

    def display(self):
        for meal, quantity in self.meals.values():
            print(f"{meal.name}: {quantity}")


menu = [
    Meal("Pasta", 10, "Regular"),
    Meal("Burger", 8, "Regular"),
    Meal("Chef's Special Steak", 25, "Special")
]

while True:
    print("\nMenu:")
    for i, meal in enumerate(menu):
        print(f"{i + 1}. {meal.name} (${meal.price}) - {meal.category}")

    order = Order()
    while True:
        selection = input("\nEnter the number of the meal you want to order, or 'done' to finish ordering: ")
        if selection.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        order.add_meal(menu[int(selection) - 1], quantity)

    print("\nYour order:")
    order.display()
    print(f"Total cost: ${order.get_total()}")

    if input("\nDo you want to make another order? (yes/no) ").lower() != 'yes':
        break
