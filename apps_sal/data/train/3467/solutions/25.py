def integrate(coefficient, exponent):
    a = int(exponent + 1)
    b = int(coefficient / a)
    c = (str(b) + "x^" + str(a))
    return c
