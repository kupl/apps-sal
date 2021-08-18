def efficientCombination(n, k):
    from math import gcd

    a, b = 1, 1

    if k == 0:
        return 1

    if n - k < k:
        k = n - k

    while k:
        a *= n
        b *= k

        m = gcd(a, b)
        a //= m
        b //= m

        n -= 1
        k -= 1

    return a


def generate_diagonal(d, amt):
    diagElements = []

    for n in range(d, amt + d, 1):
        valOnDiag = efficientCombination(n, d)
        diagElements.append(valOnDiag)

    return diagElements
