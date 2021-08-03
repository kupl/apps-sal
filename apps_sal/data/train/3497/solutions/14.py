primeTable = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def isPP(n):
    for p in primeTable:
        base = round(n ** (1 / p))
        if base ** p == n:
            return [base, p]
