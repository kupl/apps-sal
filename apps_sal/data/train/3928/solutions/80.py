def billboard(name, price=30):
    q = 0
    i = 1
    while i <= len(name):
        q += price
        i += 1
    return q
