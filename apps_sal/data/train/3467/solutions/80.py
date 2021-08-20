def integrate(coefficient, exponent):
    exp = exponent + 1
    cof = int(coefficient / exp)
    list = [str(cof), 'x^', str(exp)]
    return ''.join(list)
