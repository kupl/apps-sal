def integrate(coefficient, exponent):
    return '{coef}x^{exp}'.format(coef=coefficient // (exponent + 1), exp=exponent + 1)
