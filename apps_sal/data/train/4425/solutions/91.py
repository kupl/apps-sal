from math import floor

def mango(quantity, price):
    return (quantity-floor(quantity/3))*price
