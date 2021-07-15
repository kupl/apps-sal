from functools import reduce
from itertools import filterfalse

def segments(m, a):
    return list(filterfalse(reduce(set.union, (set(range(x, y+1)) for x,y in a), set()).__contains__, range(0, m+1)))
