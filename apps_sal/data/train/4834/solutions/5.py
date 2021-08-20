import math
KnownPrimes = []


def backwardsPrime(start, stop):
    k = math.ceil((start - 1) / 6)
    (Prime, p1, p2) = ([], 0, 0)
    while p1 <= stop or p2 <= stop:
        (p1, p2) = (6 * k - 1, 6 * k + 1)
        p1x = int(str(p1)[::-1])
        p2x = int(str(p2)[::-1])
        if not p1 == p1x and IsPrime(p1) and IsPrime(p1x) and (p1 <= stop):
            Prime.append(p1)
        if not p2 == p2x and IsPrime(p2) and IsPrime(p2x) and (p2 <= stop):
            Prime.append(p2)
        k = k + 1
    return Prime


def TryComposite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


def IsPrime(n, PrecisionForHugeN=16):
    if n in KnownPrimes or n in (0, 1):
        return True
    if any((n % p == 0 for p in KnownPrimes)):
        return False
    (d, s) = (n - 1, 0)
    while not d % 2:
        (d, s) = (d >> 1, s + 1)
    if n < 1373653:
        return not any((TryComposite(a, d, n, s) for a in (2, 3)))
    if n < 25326001:
        return not any((TryComposite(a, d, n, s) for a in (2, 3, 5)))
    if n < 118670087467:
        return [not any((TryComposite(a, d, n, s) for a in (2, 3, 5, 7))), False][n == 3215031751]
    if n < 2152302898747:
        return not any((TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11)))
    if n < 3474749660383:
        return not any((TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13)))
    if n < 341550071728321:
        return not any((TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17)))
    return not any((TryComposite(a, d, n, s) for a in KnownPrimes[:PrecisionForHugeN]))
