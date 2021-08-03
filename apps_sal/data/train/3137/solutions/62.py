import math


def round_it(n):
    if len(str(math.floor(n))) * 2 + 1 == len(str(n)):
        return round(n)
    elif len(str(math.floor(n))) * 2 + 1 > len(str(n)):
        return math.floor(n)
    elif len(str(math.floor(n))) * 2 + 1 < len(str(n)):
        return math.ceil(n)
