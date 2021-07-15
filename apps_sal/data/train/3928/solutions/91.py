def billboard(name, price=30):
    t = 0
    for i in range(len(name)):
        t += price
    return t
