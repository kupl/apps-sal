def derive(coefficient, exponent): 
    result = coefficient * exponent
    output = exponent - 1
    return str(f'{result}x^{output}')
