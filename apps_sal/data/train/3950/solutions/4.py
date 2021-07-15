from itertools import combinations
from math import gcd
def first(n):
    s=str(n)
    r=0
    for i in range(1,len(s)+1):
        for t in combinations(s,i):
            r+=int(''.join(t))
    return r

def second(n):
    s=str(n)
    r=0
    for i in range(1,len(s)+1):
        for j in range(len(s)-i+1):
            r+=int(s[j:j+i])
    return r

def common_divisors(n):
    f=first(n)
    s=second(n)
    g=gcd(f,s)
    r=1
    for x in range(2,int(g**0.5)+1):
        if g%x==0:
            if x*x==g:
                r+=1
            else:
                r+=2
    return r
    
c=[common_divisors(x) for x in range(0,55000)]

def find_int_inrange(a, b):
    m=max(c[a:b+1])
    r=[m]
    for x in range(a,b+1):
        if c[x]==m:
            r.append(x)
    return r
