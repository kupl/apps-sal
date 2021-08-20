import math


def mango(quantity, price):
    print(quantity, price)
    return math.ceil(quantity / 3 * 2) * price
