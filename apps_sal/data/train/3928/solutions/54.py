def billboard(name, price=30):
    from operator import mul
    return list(map(mul, [len(name)], [price]))[0]
