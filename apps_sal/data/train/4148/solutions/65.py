import numpy as np


def sum_digits(number):
    number = int(np.sqrt(number ** 2))
    return sum([int(d) for d in str(number)])
