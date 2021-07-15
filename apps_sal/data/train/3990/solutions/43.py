def derive(coefficient, exponent): 
    mult = coefficient * exponent
    exponent -= 1
    return str(mult) + 'x^' + str(exponent)

