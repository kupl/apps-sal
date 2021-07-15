def round_it(n):
    from math import ceil, floor
    p = str(n).find('.') / (len(str(n))-1)
    return ceil(n) if p < 0.5 else floor(n) if p > 0.5 else round(n)
