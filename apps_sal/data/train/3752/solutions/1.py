def aCb(a, b):
    result = 1.0
    for i in range(b):
        result = result * (a - i) / (i + 1)
    return result


def value_at(poly_spec, x):
    answer = 0
    l = len(poly_spec)
    for (i, coeff) in enumerate(poly_spec):
        answer += coeff * aCb(x, l - i - 1)
    return round(answer, 2)
