from math import sqrt


def isPP(n):
    limit = int(sqrt(n))
    for m in range(2, limit + 1):
        k = 2
        while m ** k <= n:
            if m ** k == n:
                return [m, k]
            k += 1
