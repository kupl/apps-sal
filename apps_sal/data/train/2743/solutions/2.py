import math


def sum_average(arr):
    return math.floor(sum([sum(array) / len(array) for array in arr]))
