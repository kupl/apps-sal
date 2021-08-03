def derive(coefficient, exponent):
    x = coefficient * exponent
    y = exponent - 1
    z = str(x) + "x^" + str(y)
    return z
