from statistics import mean as m1
from numpy import mean as m2, average as m3

# Take your pick


def average(array):
    return round(sum(array) / len(array))
    return round(m1(array))
    return round(m2(array))
    return round(m3(array))
