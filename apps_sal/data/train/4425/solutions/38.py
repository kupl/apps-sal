import math


def mango(quantity, price):
    actual = math.floor(quantity / 3)
    return (quantity - actual) * price
