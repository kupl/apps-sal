def billboard(name, price=30):
    cost = 0
    for letter in name:
        cost = cost + price
    return cost
