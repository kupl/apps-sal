def integrate(coefficient, exponent):
    exponent+=1
    coefficient/=exponent
    return '{0}x^{1}'.format(int(coefficient),exponent)
