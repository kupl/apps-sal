def integrate(coefficient, exponent):
    ex = exponent + 1
    cof = int(coefficient / ex)
    return str(cof) + "x^" + str(ex)
