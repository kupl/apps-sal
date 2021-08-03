import math


def heron(a, b, c):
    d = (a + b + c) / 2
    return round(math.sqrt(d * (d - a) * (d - b) * (d - c)), 2)
