from fractions import gcd
from functools import reduce

def solution(a):
    return len(a) * reduce(gcd, a)
