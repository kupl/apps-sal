def integrate(coefficient, exponent):
    exponent += 1
    coefficient = coefficient // exponent
    return "{0}x^{1}".format(coefficient,exponent)

