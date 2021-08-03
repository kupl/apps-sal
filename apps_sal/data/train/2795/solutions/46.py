import math


def cockroach_speed(s):
    a = s * 1000 * 100 / 60 / 60
    b = math.floor(a)
    return b
