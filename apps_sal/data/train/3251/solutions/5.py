from collections import defaultdict


def primeFactors(n):
    factors = defaultdict(int)
    n_prime = n
    for i in range(2, int(n ** 0.5) + 1):
        while not n_prime % i:
            factors[i] += 1
            n_prime /= i
    if n_prime != 1:
        factors[n_prime] += 1

    def f(x, y):
        return '(%d)' % x if y is 1 else '(%d**%d)' % (x, y)
    return ''.join((f(k, factors[k]) for k in sorted(factors)))
