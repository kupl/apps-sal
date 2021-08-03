def integrate(coefficient, exponent):
    a = int(coefficient / (exponent + 1))
    b = (exponent + 1)
    return str(a) + "x" + "^" + str(b)
