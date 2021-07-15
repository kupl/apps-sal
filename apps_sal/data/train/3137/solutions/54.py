from math import floor, ceil

def round_it(n):
    sn = str(n)
    i = sn.index('.')
    if len(sn) % 2 and i == len(sn) // 2:
        return round(n)
    elif i < len(sn) // 2:
        return ceil(n)
    
    return floor(n)
