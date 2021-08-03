import numpy as np


def sum_of_minimums(numbers):
    minimums = []
    for n in numbers:
        minimums.append(np.min(n))
    return np.sum(minimums)
