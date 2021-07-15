def derive(coefficient, exponent): 
    new_coeff = coefficient * exponent
    new_expo = exponent -1
    return str(new_coeff) + "x^" + str(new_expo)
