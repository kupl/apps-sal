from math import ceil, floor
def round_it(n):
    x,y = str(n).split(".")
    return ceil(n) if len(x) < len(y) else floor(n) if len(x) > len(y) else round(n)
