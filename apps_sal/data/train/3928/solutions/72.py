def billboard(name, price=30):
    total = 0
    for i in range(1, len(name) + 1):
        total += price
    return total
