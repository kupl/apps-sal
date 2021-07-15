def billboard(name, price=30):
    r = 0
    for i in range(len(name)):
        r += price
    return r
