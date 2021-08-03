menu = "Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke".split()


def get_order(order):
    return " ".join(item for item in menu for _ in range(order.count(item.lower())))
