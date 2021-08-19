from collections import Counter


def prime_factors(n):
    p = []
    while n % 2 == 0:
        p.append(2)
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            p.append(i)
            n /= i
    if n > 2:
        p.append(int(n))
    return p


def f(n):
    fac = Counter(prime_factors(n))
    re = 1
    for i in fac.keys():
        re *= fac[i] * i ** (fac[i] - 1)
    return re
