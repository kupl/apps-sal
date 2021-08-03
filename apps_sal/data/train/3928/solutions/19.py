def billboard(name, price=30):
    l = [price for i in range(1, len(name) + 1)]
    return sum(l)
