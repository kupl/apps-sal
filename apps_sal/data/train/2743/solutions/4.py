import math


def sum_average(arr):
    total = 0
    for x in arr:
        total += sum(x) / len(x)
    return math.floor(total)
