from math import ceil, sqrt


def squared(l):
    return [x**2 for x in l]


def divisors(m):
    s = sqrt(m)
    k = ceil(s)
    aux = [d for d in range(1, k) if m % d == 0]
    aux += [m // d for d in aux]
    if k == s:
        aux.append(k)
    return aux


def is_square(m):
    return ceil(sqrt(m)) == sqrt(m)


def list_squared(m, n):
    return [[k, s] for (k, s) in [(k, sum(squared(divisors(k)))) for k in range(m, n + 1)] if is_square(s)]
