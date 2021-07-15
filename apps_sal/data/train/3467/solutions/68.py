def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coeff = coefficient / new_exponent
    s = str(int(new_coeff)) + "x^" + str(new_exponent)
    return s
