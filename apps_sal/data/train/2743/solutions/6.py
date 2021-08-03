import numpy as np
from math import floor


def sum_average(arr):
    return floor(sum(map(np.average, arr)))
