def billboard(name, price=30):
    x = 0
    for i in range(len(name)):
        x = x + price
    return x
