def derive(coefficient, exponent):
    coef = str(coefficient * exponent)
    exp = str(exponent - 1)
    return coef + 'x^' + exp
