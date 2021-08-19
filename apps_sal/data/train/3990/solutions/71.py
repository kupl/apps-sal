def derive(coefficient, exponent):
    product = coefficient * exponent
    result_from_subtract = exponent - 1
    result = str(product) + 'x' + '^' + str(result_from_subtract)
    return result
