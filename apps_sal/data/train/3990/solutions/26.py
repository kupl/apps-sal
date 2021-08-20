def derive(coefficient, exponent):
    sum = coefficient * exponent
    exponent = exponent - 1
    return f'{sum}x^{exponent}'
