from functools import *


def array_plus_array(arr1, arr2):
    return int(reduce(lambda x, y: x + y, list(map(lambda x, y: x + y, arr1, arr2))))
