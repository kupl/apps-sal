import math


def does_fred_need_houseboat(x, y):
    r = (x * x + y * y) ** 0.5
    s = math.pi * r * r / 2
    return math.ceil(s / 50)
