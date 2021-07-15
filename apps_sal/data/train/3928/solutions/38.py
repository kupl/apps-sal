def billboard(name, price=30):
    return sum([price for i in range(1, len(name)+1)])
