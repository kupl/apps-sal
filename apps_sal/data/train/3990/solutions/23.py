def derive(coefficient, exponent): 
    new_exponent = str(exponent - 1)
    return str(coefficient * exponent) + 'x^' + new_exponent
