import math


def heron(a, b, c):
    s = (a + b + c) / 2
    v = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(v, 2)
