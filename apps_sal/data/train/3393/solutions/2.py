from math import floor, sqrt, pow


def sum_squared_factors(n):
    (s, res, i) = (0, [], 1)
    while i <= floor(sqrt(n)):
        if n % i == 0:
            s += i * i
            nf = n // i
            if nf != i:
                s += nf * nf
        i += 1
    if pow(int(sqrt(s)), 2) == s:
        res.append(n)
        res.append(s)
        return res
    else:
        return None


def list_squared(m, n):
    (res, i) = ([], m)
    while i <= n:
        r = sum_squared_factors(i)
        if r != None:
            res.append(r)
        i += 1
    return res
