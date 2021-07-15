from operator import mod


def mango(quantity, price):
    x = int((quantity / 3)) * 2
    r = mod(quantity, 3)
    return x * price + (r * price)
