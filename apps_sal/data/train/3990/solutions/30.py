def derive(coefficient, exponent):
    new_coeff = coefficient * exponent
    new_exp = exponent - 1
    expression = f"{new_coeff}x^{new_exp}"
    return expression
