def derive(coefficient, exponent):
    result =  coefficient * exponent
    exponent_new = exponent - 1
    result = str(result)
    exponent_new = str(exponent_new)
    return result + "x^" + exponent_new
