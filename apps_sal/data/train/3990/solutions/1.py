def derive(coefficient, exponent):
    a = coefficient * exponent
    b = exponent - 1
    txt = '{}x^{}'
    return txt.format(a, b)
