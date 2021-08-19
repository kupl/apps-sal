def billboard(name, price=30):
    cost = 0
    for i in range(0, len(name)):
        cost += price
    return cost
