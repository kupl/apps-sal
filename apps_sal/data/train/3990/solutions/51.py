def derive(coefficient, exponent):
    firstnum = coefficient * exponent
    secondnum = exponent - 1
    return str(firstnum) + 'x^' + str(secondnum)
