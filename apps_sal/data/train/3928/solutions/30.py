def billboard(name, price=30):
    # Without using multiplication
    total = 0
    for char in name:
        total += price

    return total
