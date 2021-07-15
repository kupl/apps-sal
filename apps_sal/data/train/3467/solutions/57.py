def integrate(coefficient, exponent):
    exp = exponent + 1
    coef = coefficient // exp
    return str(coef)+"x^"+str(exp)
