def billboard(name, price=30):
    builder = 0
    for x in name:
        builder = builder + price
    return builder
