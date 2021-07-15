from math import ceil, floor


def round_it(n):
    lst = str(n).split('.')
    return ceil(n) if len(lst[0]) < len(lst[1]) else floor(n) if len(lst[0]) > len(lst[1]) else round(n)
