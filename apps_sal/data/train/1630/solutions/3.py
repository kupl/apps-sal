from fractions import gcd
from functools import reduce
from itertools import count

def survivor(l):
    if 1 in l: return 0
    if len(l) < 2 or reduce(gcd,l) > 1: return -1
    if len(l) == 2: return (l[0]-1)*(l[1]-1)-1
    m,t,r,w=[True],0,0,max(l)
    for i in count(1):
        m = m[-w:] + [any(m[-n] for n in l if len(m)>=n)]
        if not m[-1]: t,r = i,0
        else: r += 1
        if r == w: break
    return t
