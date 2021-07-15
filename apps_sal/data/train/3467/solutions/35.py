def integrate(coefficient, exponent):
    integral = coefficient // (exponent + 1)
    return '{}x^{}'.format(integral, exponent + 1)
