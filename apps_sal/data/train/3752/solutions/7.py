def value_at(poly_spec, x):
    if len(poly_spec) < 2:
        return poly_spec[0] if poly_spec else 0
    l = len(poly_spec) - 1
    m = [co * binomial(x, l - i) for i, co in enumerate(poly_spec[:-1])]
    return round(float(sum(m) + poly_spec[l]), 2)


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def binomial(a, b):
    res = 1.0
    for k in range(b):
        res *= (a - k)
    return res / factorial(b)
