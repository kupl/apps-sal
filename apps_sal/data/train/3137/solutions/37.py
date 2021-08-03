from math import ceil, floor


def round_it(n):
    k = (str(n)).split('.')
    if len(k[0]) < len(k[1]):
        return ceil(n)
    if len(k[0]) > len(k[1]):
        return floor(n)
    return round(n)
