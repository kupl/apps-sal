def derive(coefficient, exponent):
    result = coefficient * exponent
    exponent -= 1
    return str(result) + 'x' + '^' + str(exponent)
