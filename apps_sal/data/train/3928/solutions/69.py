def billboard(name, price=30):
    r = 0
    for _ in name:
        r += price
    return r
