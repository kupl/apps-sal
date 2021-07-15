from math import ceil, floor

def round_it(n):
    str_n = str(n)
    x = str_n.split('.')[0]
    y = str_n.split('.')[1]
    if len(x) < len(y):
        return ceil(n)
    if len(x) > len(y):
        return floor(n)
    return round(n)

