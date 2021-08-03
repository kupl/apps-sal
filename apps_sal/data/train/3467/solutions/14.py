def integrate(coefficient, exponent):
    return str(coefficient / (exponent + 1)).rstrip('0').rstrip('.') + "x^" + str(exponent + 1)
