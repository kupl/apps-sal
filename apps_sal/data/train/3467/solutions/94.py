def integrate(coefficient, exponent):
    exponent=exponent+1
    coefficient=coefficient//exponent
    return str(coefficient) + "x" +"^" + str(exponent)
