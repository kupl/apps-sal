import numpy as np


def square_sum(numbers):
    array_sum = np.array(numbers)
    result = np.sum(array_sum ** 2)
    return result
