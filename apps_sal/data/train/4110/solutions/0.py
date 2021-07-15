from math import ceil

def matrixfy(s):
    if not s: return "name must be at least one letter"
    x  = ceil(len(s)**.5)
    it = iter(s.ljust(x*x,'.'))
    return [ [next(it) for _ in range(x)] for _ in range(x)]
