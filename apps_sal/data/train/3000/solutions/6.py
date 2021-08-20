from collections import Counter


def decompose(n):
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
    return result


def mul_power(n, k):
    r = 1
    for (p, f) in decompose(n).items():
        r *= p ** (-f % k)
    return r
