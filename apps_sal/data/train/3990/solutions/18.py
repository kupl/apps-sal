def derive(coefficient, exponent): 
    if exponent >= 2 and coefficient * exponent != 0:
        return str(coefficient * exponent) + 'x^' + str(exponent - 1) 
