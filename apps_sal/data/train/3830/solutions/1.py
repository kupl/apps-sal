from collections import Counter


def factors(n):

    def step(x):
        return 1 + 4 * x - (x - x % 2)
    (d, q, qmax) = (1, 2 + n % 2, int(n ** 0.5))
    while q <= qmax and n % q:
        q = step(d)
        d += 1
    return q <= qmax and [q] + factors(n // q) or [n]


def chain_arith_deriv(start, k):
    (n, chain) = (start, [])
    for _ in range(k):
        chain.append(n)
        fac = Counter(factors(n))
        n = sum((n // p * k for (p, k) in fac.items()))
    return chain if chain[1] > 1 else '%d is a prime number' % start
