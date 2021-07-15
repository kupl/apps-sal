def derive(coefficient, exponent): 
    # your code here
    dv = coefficient * exponent
    ex = exponent - 1
    return str(dv) + "x^" + str(ex)
