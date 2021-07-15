from functools import reduce
from math import factorial as fac
from operator import mul

def proc_arr(lst):
    stg = "".join(sorted(lst))
    p = fac(len(stg)) // reduce(mul, (fac(stg.count(d)) for d in set(stg)))
    return [p, int(stg), int(stg[::-1])]
