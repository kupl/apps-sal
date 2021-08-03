import math


def how_many_measurements(n):
    count = 0
    while n > 1:
        n = math.ceil(n / 3)
        count += 1
    return count
