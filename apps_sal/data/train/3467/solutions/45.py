def integrate(coefficient, exponent):
    x = int(coefficient / (exponent + 1))
    return str(x) + 'x^' + str(exponent + 1)
