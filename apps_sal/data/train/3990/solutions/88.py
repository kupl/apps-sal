def derive(coefficient, exponent): 
    if exponent > 1:
        x = str(coefficient * exponent)
        y = str(exponent - 1)
        
        return str(x + "x^" + y)
