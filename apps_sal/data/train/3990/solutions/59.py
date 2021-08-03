def derive(coefficient, exponent):
    result = coefficient * exponent
    print(result)
    return str(result) + "x^" + str(exponent - 1)
