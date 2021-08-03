import math


def mango(quantity, price):
    free_mangos = math.floor(quantity / 3)
    return (quantity - free_mangos) * price
