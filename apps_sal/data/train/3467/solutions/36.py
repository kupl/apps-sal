def integrate(coefficient, exponent):
    exponent += 1
    a = int(coefficient / exponent)
    return str(a) + 'x^' + str(exponent)
