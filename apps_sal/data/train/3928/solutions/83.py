def billboard(name, price=30):
    return sum(len(name) for _ in range(0, price))
