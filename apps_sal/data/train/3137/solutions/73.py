import math
def round_it(n):
    l, r = [len(x) for x in str(n).split('.')]
    if r > l:
        return math.ceil(n)
    elif r < l:
        return math.floor(n)
    else:
        return round(n)
