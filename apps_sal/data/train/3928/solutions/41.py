import numpy as np


def billboard(name, price=30):
    return np.dot(len(name), price)
