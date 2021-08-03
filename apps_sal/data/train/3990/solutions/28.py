def derive(coefficient, exponent):
    if exponent == 2:
        return str(coefficient * exponent) + "x^2"
    else:
        return str(coefficient * exponent) + "x^" + str(exponent - 1)
