def derive(coefficient, exponent):
    a = str(coefficient * exponent)
    b = str(exponent - 1)
    return(f'{a}x^{b}')
