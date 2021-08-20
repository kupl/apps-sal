import operator
res = 0


def billboard(name, price=30):
    return sum([len(name) for i in range(price)])
