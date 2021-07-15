def derive(coefficient, exponent): 
    return "{}x^{}".format(str(coefficient*exponent), exponent-1) if exponent>2 else str(coefficient*exponent)+"x"
