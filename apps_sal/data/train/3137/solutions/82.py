import math

def round_it(n):
    p = str(n).split('.')
    if len(p[0]) < len(p[1]):
        return math.ceil(n)
    elif len(p[0]) > len(p[1]):
        return math.floor(n)
    else:
        return round(n)
