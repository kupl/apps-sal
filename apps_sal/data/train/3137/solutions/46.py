from math import floor, ceil

def round_it(n):
    d = str(n).split('.')
    return ceil(n) if len(d[0]) < len(d[1]) else floor(n) if len(d[0]) > len(d[1]) else round(n)

