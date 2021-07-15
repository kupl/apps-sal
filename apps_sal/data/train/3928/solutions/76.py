def billboard(name, price=30):
    p = 0
    for i in range(len(name)):
        p += price
    return p
