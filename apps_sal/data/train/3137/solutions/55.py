import math


def round_it(n):
    (dl, dr) = [len(d) for d in str(n).split('.')]
    if dl == dr:
        return round(n)
    elif dl > dr:
        return math.floor(n)
    else:
        return math.ceil(n)
