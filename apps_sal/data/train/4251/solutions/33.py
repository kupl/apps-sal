import numpy as np


def difference_of_squares(n):
    return sum(range(1, n + 1)) ** 2 - sum(np.array(range(1, n + 1)) ** 2)
