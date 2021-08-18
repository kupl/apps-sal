def derive(coefficient, exponent):

    result = coefficient * exponent
    re = exponent - 1
    return "{}x^{}".format(result, re)
