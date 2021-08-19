def billboard(name, price=30):
    total = 0
    i = 0
    while i < len(name):
        total += price
        i += 1
    return total
