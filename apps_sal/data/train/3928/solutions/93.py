def billboard(name, price=30):
    x = 0
    for i in [i for i in name]:
        x+=price
    return x
