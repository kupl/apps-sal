import math
def round_it(n):
    f = len
    k = str(n)
    k=k.split('.')
    a,b = k
    if f(a)<f(b): return math.ceil(n)
    elif f(a)>f(b): return math.floor(n)
    else: return round(n)
    

