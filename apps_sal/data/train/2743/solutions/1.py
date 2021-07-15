from statistics import mean
from math import floor

def sum_average(arr):
    return floor(sum(mean(lst) for lst in arr))
