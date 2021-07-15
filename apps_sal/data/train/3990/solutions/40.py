def derive(coefficient, exponent): 
    result = coefficient*exponent
    exponent1 = exponent - 1
    return f'{result}x^{exponent1}'
