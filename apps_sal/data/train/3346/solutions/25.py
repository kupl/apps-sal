import numpy 

def sieve(n):
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p*p//3::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]

primes = sieve(12*10**6)

def gap(g,m,n): 
    l = 0 
    r = len(primes)-1 
    start = 10**8 
    while l<=r:
        mid = l+(r-l)//2 
        if primes[mid] >= n:
            r = mid-1 
        elif primes[mid] < m: 
            l = mid+1 
            if start == 10**8:
                start = mid 
            else:
                start = max(mid,start) 
        elif m <= primes[mid] <= n:
            start = min(mid,start) 
            r = mid-1 
    
    for i in range(start,len(primes)): 
        if primes[i] > n:
            break
        if primes[i] < m:
            continue 
        if primes[i+1] - primes[i] == g:
            return [primes[i],primes[i+1]]
    return None 
