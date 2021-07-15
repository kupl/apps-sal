import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    return  reduce(op.mul, range(n, n-r, -1), 1)// reduce(op.mul, range(1, r+1), 1)

def generate_diagonal(n, l):
    mx = []
    i,j = n,0
    while i < n+l:
        mx.append(ncr(i,j))
        i+=1
        j+=1
    return mx
