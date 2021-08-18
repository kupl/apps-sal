import numpy as np


def nth_smallest(arr, pos):
    arr = sorted(arr)
    return arr[pos - 1]
