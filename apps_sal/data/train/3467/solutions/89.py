def integrate(coefficient, exponent):
    e1 = exponent + 1
    r  = int(coefficient / e1)
    return '{}x^{}'.format(r,e1)
