def billboard(name, price=30):
    cost = 0
    print(name)
    for i in range(len(name)):
        cost += price
    return cost
