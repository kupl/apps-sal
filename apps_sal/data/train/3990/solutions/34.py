def derive(coefficient, exponent): 
    return ''.join(str(int(coefficient * exponent)) + 'x^' + str(int(exponent) - 1))
