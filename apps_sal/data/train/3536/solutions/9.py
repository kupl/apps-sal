from functools import reduce
from operator import mul

def cog_RPM(cogs, n):
    f = lambda l: 1 if len(l) < 2 else reduce(mul, [ -x/y for x,y in zip(l,l[1:]) ] )
    return [ f(cogs[:n+1][::-1]), f(cogs[n:]) ]
