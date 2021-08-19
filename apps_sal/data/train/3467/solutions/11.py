def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = int(coefficient / new_exponent)
    return str(new_coefficient) + 'x^' + str(new_exponent)
