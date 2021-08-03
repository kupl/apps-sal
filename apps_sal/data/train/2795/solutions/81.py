import math


def cockroach_speed(s):
    temp = (s * 1000 * 100) / 3600
    result = math.floor(temp)
    return result
