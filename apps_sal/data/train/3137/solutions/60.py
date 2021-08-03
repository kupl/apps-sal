import math


def round_it(n):
    x, y = str(n).split('.')
    x_string = len(str(x))
    y_string = len(str(y))
    if x_string < y_string:
        return math.ceil(n)
    if x_string > y_string:
        return math.floor(n)
    return round(n)
