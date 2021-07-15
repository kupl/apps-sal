def billboard(name, price=30):
    a = len(name)
    cost = 0
    for i in range(1, a+1, 1):
        cost += price
    return cost
