import numpy as np


def row_sum_odd_numbers(n):
    return sum(np.linspace(n ** 2 - (n - 1), n ** 2 + n - 1, n))
