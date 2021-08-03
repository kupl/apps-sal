def derive(coefficient, exponent):
    coeff = coefficient * exponent
    return str(coeff) + "x^" + str(exponent - 1)
