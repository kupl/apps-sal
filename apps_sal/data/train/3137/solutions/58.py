import math

def round_it(n):
    if (len(str(n)) - 1) / 2 > str(n).index('.'):
        return math.ceil(n)
    elif (len(str(n)) - 1) / 2 < str(n).index('.'):
        return math.floor(n)
    else:
        return round(n)
