from math import ceil, floor


def round_it(n):
    """Round number based on decimal position"""
    ls, rs = str(n).split('.')
    if len(ls) < len(rs):
        return ceil(n)
    if len(ls) > len(rs):
        return floor(n)
    return round(n)
