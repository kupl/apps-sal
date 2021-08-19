def comb(a, b):
    r = 1
    s = 1
    for i in range(1, b + 1):
        r *= a - i + 1
        s *= i
    return r / s


def value_at(poly_spec, x):
    r = 0
    for (i, c) in enumerate(poly_spec[::-1]):
        r += c * comb(x, i)
    return round(r, 2)
