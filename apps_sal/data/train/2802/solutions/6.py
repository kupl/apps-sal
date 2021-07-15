from functools import reduce
from operator import mul

def per(n):
    result = []
    s = str(n)
    while len(s) > 1:
        result.append(reduce(mul, map(int, s)))
        s = str(result[-1])
    return result
