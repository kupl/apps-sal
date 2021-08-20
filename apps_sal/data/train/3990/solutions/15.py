def derive(coefficient, exponent):
    coefficient2 = coefficient * exponent
    exponent2 = exponent - 1
    ans = '' + str(coefficient2) + 'x^' + str(exponent2)
    return ans
