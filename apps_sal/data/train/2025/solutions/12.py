import math
import collections

def factorize(n):
    ''' returns a list of prime factors of n.
    ex. factorize(24) = [2, 2, 2, 3]
    source: Rossetta code: prime factorization (slightly modified)
    http://rosettacode.org/wiki/Prime_decomposition#Python:_Using_floating_point
    '''
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = int(math.floor(math.sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + factorize(n//q) or [n]

def primes2(limit):
    ''' returns a list of prime numbers upto limit.
    source: Rossetta code: Sieve of Eratosthenes
    http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above
    '''
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]


n = int(input())

def solve(n):
    if n == 1:
        print(0)
        return
    primes = primes2(n)
    record = {p:0 for p in primes}
    for m in range(2, n+1):
        facs = factorize(m)
        counts = collections.Counter(facs)
        for p, c in counts.items():
            if c > record[p]:
                record[p] = c
    q = sum(record.values())
    print(q)
    nums = []
    for p, c in record.items():
        for i in range(1, c+1):
            nums.append(p**i)
    if q > 0:
        print(*nums)

solve(n)
