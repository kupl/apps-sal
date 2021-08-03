def integrate(coefficient, exponent):
    return '%ix^%i' % ((coefficient / (exponent + 1)), (exponent + 1))
#     return 'x^'.join((str(coefficient // (exponent + 1)), str(exponent + 1)))
