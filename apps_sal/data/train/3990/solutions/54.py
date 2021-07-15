def derive(coefficient, exponent): 
    coEx = coefficient * exponent
    expoMinus = exponent-1

    return str(coEx) + "x^" + str(expoMinus)
