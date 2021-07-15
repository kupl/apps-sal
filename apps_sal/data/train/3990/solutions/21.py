def derive(coefficient, exponent): 
    n = coefficient * exponent
    expo = exponent - 1
    return(str(n)+"x^"+str(expo))
