import functools
import itertools


def rthn_between(a, b):
    k1 = len(str(b))+1
    k0 = len(str(a))-1
    harshads = set.union(*map(n_part_harshad, range(k0, k1)))
    return  sorted( [i for i in harshads if i in range(max(10,a),b+1) ] )

@functools.lru_cache(None)
def n_part_harshad(k):
    vals = set(range(10))
    if k < 1: return vals - {0}
    prevs = n_part_harshad(k-1)
    groups = (10*a+b for a,b in  itertools.product(prevs, vals) )
    return set(filter(part_harshad, groups))

def r_harshad(n):
    k = str(n)
    vals = (int(k[:i]) for i in range(1,len(k)+1) )
    return n>9 and  all( map(part_harshad, vals))

@functools.lru_cache(None)
def part_harshad(n):
    return n% dig_sum(n)==0
    
def dig_sum(n):
    return sum(map(int,str( n)))
