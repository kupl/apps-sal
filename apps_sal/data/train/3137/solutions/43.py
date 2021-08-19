import math


def round_it(n):
    d_split = str(n).split('.')
    if len(d_split[0]) > len(d_split[1]):
        return math.floor(n)
    elif len(d_split[1]) > len(d_split[0]):
        return math.ceil(n)
    else:
        return round(n)
