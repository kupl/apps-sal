from functools import  reduce as R
from collections import Counter as C
from math import gcd as G
def has_subpattern(s): 
    s = C(s)
    k =  R(G,set(s.values()))
    li = [i * (j // k) for i, j in s.items()]
    return ''.join(sorted(li))
