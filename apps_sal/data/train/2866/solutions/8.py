from collections import defaultdict


def prime_factor(n):
    r = defaultdict(int)
    while n % 2 == 0:
        r[2] += 1
        n //= 2
    x = 3
    while n > 1 and x * x <= n:
        while n % x == 0:
            r[x] += 1
            n //= x
        x += 2
    if n > 1:
        r[n] += 1
    return r


def mobius(n):
    fs = prime_factor(n)
    if max(fs.values()) > 1:
        return 0
    elif len(fs.keys()) % 2 == 0:
        return 1
    else:
        return -1
