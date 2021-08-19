import numpy as np


def mango(quantity, price):
    return (quantity - np.floor(quantity / 3)) * price
