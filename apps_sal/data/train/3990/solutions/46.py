def derive(coefficient, exponent): 
    result = ""
    product = coefficient*exponent
    exponent = exponent -1
    result = str(product) + "x^" + str(exponent)
    # your code here
    return result
    pass
