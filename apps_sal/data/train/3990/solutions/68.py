def derive(coefficient, exponent): 
    prod = coefficient * exponent
    exp = exponent - 1
    return "{}x^{}".format(prod, exp)
