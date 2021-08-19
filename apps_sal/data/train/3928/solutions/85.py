def billboard(name, price=30):
    # len(name) * price
    total = 0
    for x in name:
        if x:
            total += price
    return total
