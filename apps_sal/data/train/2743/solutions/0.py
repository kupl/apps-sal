from statistics import mean
from math import floor


def sum_average(arr):
    return floor(sum(map(mean, arr)))
