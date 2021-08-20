def binom(x, k):
    r = 1
    for i in range(1, k + 1):
        r *= (x - i + 1) / i
    return r


def value_at(poly_spec, x):
    r = 0
    for (k, c) in enumerate(poly_spec[::-1]):
        r += c * binom(x, k)
    return round(r, 2)
