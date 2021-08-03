import numpy as np


def maximum_product(arr):
    return -max((np.multiply.reduce(arr[:c] + arr[c + 1:]), -a) for c, a in enumerate(arr))[1]
