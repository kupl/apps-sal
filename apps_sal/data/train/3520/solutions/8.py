import itertools
compress = itertools.compress 
def sieve(n): 
    r = [False,True] * (n//2) +[True]
    r[1],r[2] = False,True 
    for i in range(3,int(n**.5)+1): 
        if r[i]: 
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    r = list(compress(range(len(r)),r))
    if r[-1] % 2 == 0:
        return r[:-1]
    return r
primes = set(sieve(2*10**7))
maxi = max(primes) 
def step(g, m, n):
    for i in range(m,n+1): 
        if i > maxi or i+g > n:
            break 
        if i in primes and i+g in primes:
            return [i,i+g]
    return None 
