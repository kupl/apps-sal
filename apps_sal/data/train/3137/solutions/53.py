def round_it(n):
    import math
    tmp=str(n).index('.')
    bef_dot=tmp
    after_dot=len(str(n))-tmp-1
    if bef_dot<after_dot: return math.ceil(n)
    if bef_dot>after_dot: return math.floor(n)
    if bef_dot==after_dot: return round(n)
