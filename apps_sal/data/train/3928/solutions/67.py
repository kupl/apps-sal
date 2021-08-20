def billboard(name, price=30):
    p = 0
    if price == 30:
        for c in range(len(name)):
            p += 30
        return p
    if price != 30:
        for c in range(len(name)):
            p += price
        return p
