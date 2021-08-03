import numpy
import math


def sum_average(arr):
    print(arr)
    total = 0
    for item in arr:
        print(numpy.mean(item))
        total += numpy.mean(item)
    return math.floor(total)
