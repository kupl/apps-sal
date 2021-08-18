def derive(coefficient, exponent):
    dv = coefficient * exponent
    ex = exponent - 1
    return str(dv) + "x^" + str(ex)
