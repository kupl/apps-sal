def derive(coefficient, exponent):
    product = coefficient * exponent
    x = exponent - 1
    return str(product) + 'x^' + str(x)
