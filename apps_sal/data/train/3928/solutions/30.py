def billboard(name, price=30):
    total = 0
    for char in name:
        total += price

    return total
