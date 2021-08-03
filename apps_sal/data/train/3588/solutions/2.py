import numpy as np


def quadratic(*args):
    return tuple(np.poly(args))
