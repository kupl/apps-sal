def billboard(name, price=30):
    total_price = 0
    for char in range(len(name)):
        total_price += price
    return total_price
