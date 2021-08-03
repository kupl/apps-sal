import math


def heron(a, b, c):
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
