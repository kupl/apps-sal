import sys
if sys.version_info.major >= 3:
    from functools import reduce
if sys.version_info < (3,5):
    from fractions import gcd
elif sys.version_info >= (3,5):
    from math import gcd

def solution(a):
    return reduce(gcd, a) * len(a)
