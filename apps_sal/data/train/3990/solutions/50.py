def derive(coefficient, exponent):
    new_coeff = coefficient * exponent
    result = '%dx^%d'
    new_exp = exponent - 1
    return result % (new_coeff, new_exp)
