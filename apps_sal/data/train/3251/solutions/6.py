from collections import Counter


def fac(n):
    maxq = int(n ** 0.5)
    (d, q) = (1, n % 2 == 0 and 2 or 3)
    while q <= maxq and n % q != 0:
        q = 1 + d * 4 - d // 2 * 2
        d += 1
    res = Counter()
    if q <= maxq:
        res += fac(n // q)
        res += fac(q)
    else:
        res[n] = 1
    return res


def primeFactors(n):
    return ''.join((('({})' if m == 1 else '({}**{})').format(p, m) for (p, m) in sorted(fac(n).items())))
