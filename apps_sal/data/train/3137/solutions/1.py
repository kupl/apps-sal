from math import floor, ceil

def round_it(n):
    l, r = [len(x) for x in str(n).split('.')]
    if r > l:
        return ceil(n)
    elif r < l:
        return floor(n)
    else:
        return round(n)
