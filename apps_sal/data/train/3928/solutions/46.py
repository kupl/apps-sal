def billboard(name, price=30):
    cost = 0
    for s in name:
        cost += price
    return cost
