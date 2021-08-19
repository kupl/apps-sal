from collections import Counter


def primeFactors(n):
    c = Counter()
    while n % 2 == 0:
        c[2] += 1
        n //= 2
    d = 3
    while n > 1:
        while n % d == 0:
            c[d] += 1
            n //= d
        d += 2
    return ''.join((f'({key}**{value})' if value > 1 else f'({key})' for (key, value) in sorted(c.items())))
