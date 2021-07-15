def derive(coefficient, exponent): 
    coeff = coefficient * exponent
    exp = exponent - 1
    return f'{coeff}x^{exp}'
