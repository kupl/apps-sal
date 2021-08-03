from operator import mul


def billboard(name, price=30):
    return mul(len(name), price)
