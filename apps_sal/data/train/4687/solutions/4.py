from itertools import count

dec = [[],[],[1]]
primes = [2]

def genPrimes():
    for x in count(3,2):
        sq = int(x**.5)
        if all(p>sq or x%p for p in primes):
            yield x
    
primGen = genPrimes()

def genPrimesUpTo(n):
    while primes[-1] < n:
        primes.append(next(primGen))

def genPrimeDivs(n):
    genPrimesUpTo(n)
    dec.append(dec[-1][:])                                # Duplicate last factorial decomposition
    for i,p in enumerate(primes):
        while not n%p:
            n //= p
            while i >= len(dec[-1]): dec[-1].append(0) 
            dec[-1][i] += 1
            if n<2: break
    

def decomp(n):
    while len(dec) <= n:
        genPrimeDivs(len(dec))
    return " * ".join(str(p) if c==1 else "{}^{}".format(p,c) for p,c in zip(primes,dec[n]))
