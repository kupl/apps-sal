import numpy as np
from scipy import ndimage


def first_tooth(a):
    d = ndimage.convolve(a, [-1, 2, -1], mode="nearest")
    m = np.argwhere(d == d.max())
    return m[0][0] if len(m) == 1 else -1
