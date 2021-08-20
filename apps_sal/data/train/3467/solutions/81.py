def integrate(coefficient, exponent):
    a = round(coefficient / (exponent + 1))
    b = exponent + 1
    return '{}x^{}'.format(a, b)
