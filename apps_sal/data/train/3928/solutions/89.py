def billboard(name, price=30):
    i = 0
    x = 0
    b = len(name)
    while i < b:
        x = x + price
        i += 1
    return x
