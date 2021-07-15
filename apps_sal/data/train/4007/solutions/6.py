from fractions import gcd
from functools import reduce

def finding_k(arr):
    fr = [x-min(arr) for x in arr]
    if all(v == 0 for v in fr):
        return -1
    else:
        return  reduce(lambda x,y:gcd(x,y),fr)
