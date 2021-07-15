def integrate(coefficient, exponent):
    exp = exponent + 1
    coeff = int(coefficient / exp)
    return f'{coeff}x^{exp}'
