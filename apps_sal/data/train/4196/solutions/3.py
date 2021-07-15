from itertools import compress 
def sieve(n):
    r = [False,True] * (n//2) + [True] 
    r[1],r[2] = False,True 
    for i in range(3,int(n**.5)+1,2): 
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    r = list(compress(range(len(r)),r))
    if r[-1] %2 == 0:
        return r[:-1]
    return r 

primes = sieve(25000) 

def summationOfPrimes(n): 
    l = 0
    r = len(primes)-1 
    res = 0 
    while l<=r:
        mid = l+(r-l)//2 
        if primes[mid] == n:
            return sum(primes[:mid+1])
        elif primes[mid] < n:
            res = max(mid+1,res)
            l = mid+1
        else:
            r = mid-1 
    return sum(primes[:res])
