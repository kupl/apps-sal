from math import gcd
try:
    from math import prod
except ImportError:

    def prod(l, p=1):
        for n in l:
            p *= n
        return p
max_n = 1000000000


def DPC_sequence(s):
    if s[0] == 'C':
        return -1
    primes = list(find_primes(len(s)))
    pf = []
    for p in primes:
        if s[p - 1] == 'C':
            return -1
        if s[p - 1] == 'D':
            pf.append(p)
    for p in pf:
        for i in range(2 * p - 1, len(s), p):
            if s[i] == 'P':
                return -1
    base = prod(pf)
    nmax = min(prod(primes), max_n)
    for n in range(base, nmax, base):
        if test(s, n):
            return n
    return -1


def test(s, n):
    for k in range(2, len(s) + 1):
        c = s[k - 1]
        if c == 'D':
            if n % k != 0:
                return False
        elif (gcd(n, k) == 1) != (c == 'P'):
            return False
    return True


def find_primes(n):
    if n < 2:
        return
    yield 2
    s = list(range(1, n + 1, 2))
    mroot = int(n ** 0.5)
    half = (n + 1) // 2
    i = 1
    m = 3
    while m <= mroot:
        if s[i]:
            yield s[i]
            j = m * m // 2
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m += 2
    for x in s[i:]:
        if x:
            yield x
