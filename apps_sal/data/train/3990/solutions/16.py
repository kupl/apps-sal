def derive(coefficient, exponent):
    a = coefficient * exponent
    b = exponent - 1
    return str(a) + 'x^' + str(b)
