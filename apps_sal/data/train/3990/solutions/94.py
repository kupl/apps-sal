def derive(coefficient, exponent):

    product = coefficient * exponent

    str1 = ""
    exponent -= 1

    str1 += str(product) + 'x' + '^' + str(exponent)

    return str1
