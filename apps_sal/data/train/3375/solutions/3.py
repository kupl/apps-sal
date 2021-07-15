from itertools import accumulate as acc
from math import floor

def going(n):
    return floor(1e6*(1 + sum(1/x for x in acc(range(n, 1, -1), lambda a, b: a*b))))/1e6
