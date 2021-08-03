from scipy.special import comb
from collections import Counter


def factorize_exponents(n):
    result = Counter()
    while n % 2 == 0:
        result[2] += 1
        n //= 2
    k = 3
    m = int(n ** 0.5)
    while k <= m:
        if n % k == 0:
            result[k] += 1
            n //= k
            m = int(n ** 0.5)
        else:
            k += 2
    if n > 1:
        result[n] += 1
    return list(result.values())


def multiply(n, k):
    factorized = factorize_exponents(n)
    total = 1
    for exp in factorized:
        total *= comb(exp + k - 1, k - 1, exact=True)
    return total
