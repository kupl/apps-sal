def integrate(coefficient, exponent):
    return '{co}x^{exp}'.format(co=coefficient // (exponent + 1), exp=exponent + 1)
