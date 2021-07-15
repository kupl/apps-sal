def integrate(coefficient, exponent):
    a = coefficient / (exponent + 1)
    a = int(a)
    return f'{a}x^{exponent + 1}'
