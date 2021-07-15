from functools import reduce
from itertools import count
coefs = [
    [22, 13, 4],
    [365, 167, 50, 14],
    [5415, 2130, 627, 177, 51],
    [75802, 27067, 7897, 2254, 661, 202],
    [1025823, 343605, 100002, 28929, 8643, 2694, 876]
]
def f(n): return sum(c*int(d) for c,d in zip(coefs[len(str(n))-3], str(n)))

def find(n,z):
    t = f(n)+z
    for nf in count(n):
        if f(nf) > t: return nf
