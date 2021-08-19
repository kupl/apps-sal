def derive(coefficient, exponent):
    # your code here
    product = coefficient * exponent
    result_from_subtract = exponent - 1

    result = str(product) + "x" + "^" + str(result_from_subtract)
    return result
