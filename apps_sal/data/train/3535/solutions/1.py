MENU = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def get_order(order):
    result = []
    for item in MENU:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)
