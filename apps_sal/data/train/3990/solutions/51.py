def derive(coefficient, exponent):
    # your code here
    firstnum = coefficient * exponent
    secondnum = exponent - 1
    return (str(firstnum) + 'x^' + str(secondnum))
