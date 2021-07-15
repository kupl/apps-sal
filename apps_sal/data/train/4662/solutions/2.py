from itertools import compress
def sieve(n): 
    n += 1
    r = [False,True] * (n//2) + [True] 
    r[1] = False
    r[2] = True 
    for i in range(3,int(n**.5)+1,2): 
        if r[i]: 
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    r = list(compress(range(len(r)),r))
    if r[-1] %2 == 0:
        return r[:-1]
    return r

primes = set(sieve(10**6))
res = [] 
factors = {'2','3','5','7'}
for i in range(1,10**6): 
    if i not in primes and set(str(i)).isdisjoint(factors): 
        res.append(i)

def solve(n):
    return res[n] 
