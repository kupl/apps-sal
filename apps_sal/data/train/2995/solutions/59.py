import math

def sum_mul(n, m):
    if n<=0 or m<=0: return 'INVALID'
    s=0
    i=n
    while i<m:
        s+=i
        i+=n
    return s
