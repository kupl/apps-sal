from fractions   import gcd
from collections import defaultdict
from functools   import reduce

def lcm(a,b):        return int(a*b/gcd(a,b))
def full_lcm(*args): return reduce(lcm, args)

def DPC_sequence(s):
    DPC_dct = defaultdict(set)
    for i,c in enumerate(s,1): DPC_dct[c].add(i)
    n = full_lcm(*DPC_dct['D'])
    return  -1 if any( gcd(n, x) in [1, x] for x in DPC_dct['C']) or any( gcd(n, x) != 1 for x in DPC_dct['P']) else n

