def billboard(name, price=30):
    print(('name:', name))
    return sum([price for x in name])
