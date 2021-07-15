def integrate(coefficient, exponent):
    integ_coeff = coefficient / (exponent + 1)
    integ_expo = exponent + 1
    
    return str(int(integ_coeff)) + "x^" + str(exponent + 1)
