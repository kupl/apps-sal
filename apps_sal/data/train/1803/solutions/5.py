from itertools import combinations
from functools import reduce

def max_pal(n):
    if n < 10: return n
    a = [0]*10
    while n:
        n,d = divmod(n,10)
        a[d] += 1
    s = ""
    for d,n in enumerate(a):
        c = str(d)
        while n > 1:
            s = c+s+c
            n -= 2
        a[d] = n
    if s.startswith('0'): s = ""
    i = next((i for i in range(9,-1,-1) if a[i]),-1)
    if ~i: s = s[:len(s)>>1] + str(i) + s[len(s)+1>>1:]
    return int(s)

def numeric_palindrome(*a):
    z = 0 in a
    o = a.count(1)
    a = [n for n in a if n > 1]
    if o: a.append(1)
    a = [max_pal(reduce(int.__mul__,r)) for i in range(2,len(a)+1) for r in combinations(a,i)]
    if z: a.append(0)
    if o > 1: a.append(1)
    return max(a)
