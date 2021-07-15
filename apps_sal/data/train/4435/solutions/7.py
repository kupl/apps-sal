from functools import  reduce as R
from collections import Counter as C
from math import gcd as G
def has_subpattern(s): 
    return R(G,set(C(s).values())) != 1
