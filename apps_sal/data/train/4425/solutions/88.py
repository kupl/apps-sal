import math


def mango(quantity, price):
    a = math.floor(quantity / 3)
    return math.floor((quantity - a) * price)
