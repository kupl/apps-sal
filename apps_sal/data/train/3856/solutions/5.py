import itertools
compress = itertools.compress


def primeSieve(n):
    if n < 2:
        return []
    r = [False, True] * (n // 2) + [True]
    (r[1], r[2]) = (False, True)
    for i in range(3, int(1 + n ** 0.5), 2):
        if r[i]:
            r[i * i::2 * i] = [False] * ((n + 2 * i - 1 - i * i) // (2 * i))
    r = list(compress(list(range(len(r))), r))
    if r[-1] % 2 == 0:
        r.pop()
    return r


primes = primeSieve(500000)
dicti = dict()
for i in range(len(primes)):
    dicti[primes[i]] = i + 1
primeSet = frozenset(primes)


def solve(a, b):
    sum = 0
    for i in range(a, b + 1):
        if i in primeSet:
            if dicti[i] in primeSet:
                sum += i
    return sum
