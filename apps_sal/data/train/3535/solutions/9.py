def get_order(order):
    menu = [
    "Burger",
    "Fries",
    "Chicken",
    "Pizza",
    "Sandwich",
    "Onionrings",
    "Milkshake",
    "Coke",
]
    return "".join([(item + " ") * order.count(item.lower()) for item in menu]).strip()
