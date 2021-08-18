def billboard(name, price=30):
    return sum(price for i in range(len(name)))
