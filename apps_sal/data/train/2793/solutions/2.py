from math import sqrt

def group_size(size, day):
    skip = size * (size - 1) // 2
    day += skip
    return round(sqrt(day * 2))
