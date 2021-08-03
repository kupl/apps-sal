from math import factorial as f
from functools import reduce as r
from operator import mul as m
from collections import Counter as C
def proc_arr(a): return [f(len(a)) // r(m, map(f, C(a).values())), int(''.join(sorted(a, key=int))), int(''.join(sorted(a, key=int))[::-1])]
