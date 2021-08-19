def integrate(coefficient, exponent):
    e = exponent + 1
    f = round(coefficient * (1 / e))
    return str(f) + 'x^' + str(e)
