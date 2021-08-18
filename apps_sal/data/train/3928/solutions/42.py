def billboard(name, price=30):
    pri = 0
    for i in name:
        pri += price
    return pri
