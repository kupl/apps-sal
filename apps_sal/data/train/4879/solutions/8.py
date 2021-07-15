from math import factorial as f
from operator import mul

def count_perms(m):
    rep = [[i for s in m for i in s].count(j) for j in set([i for s in m for i in s])]
    rep = [f(i) for i in rep]
    tot = (len(m)*len(m[0]))
    return f(tot)/reduce(mul, rep, 1)
