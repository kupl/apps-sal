def integrate(coefficient, exponent):
    e = exponent + 1
    coef = coefficient / e

    return "{}x^{}".format(int(coef), e)
