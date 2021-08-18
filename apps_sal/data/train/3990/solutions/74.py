def derive(coefficient, exponent):
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    result = str(new_coefficient) + 'x^' + str(new_exponent)
    return result
