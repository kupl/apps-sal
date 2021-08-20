def derive(coefficient, exponent):
    mul = coefficient * exponent
    sub = exponent - 1
    return f'{mul}x^{sub}'
