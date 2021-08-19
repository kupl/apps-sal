def integrate(coefficient, exponent):
    return '{c}x^{e}'.format(c=coefficient // (exponent + 1), e=exponent + 1)
