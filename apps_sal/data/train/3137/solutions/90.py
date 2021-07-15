def round_it(n):
    import math
    a=str(n).split('.')
    if len(a[0])<len(a[1]): return math.ceil(n)
    elif len(a[0])>len(a[1]): return math.floor(n)
    else: return round(n)
    r
