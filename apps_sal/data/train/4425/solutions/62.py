import math


def mango(quantity, price):
    return quantity * price - math.floor(quantity / 3) * price
