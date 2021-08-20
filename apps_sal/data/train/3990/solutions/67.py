def derive(coefficient, exponent):
    if exponent > 2:
        string = str(coefficient * exponent) + 'x^' + str(exponent - 1)
        return string
    else:
        string = str(coefficient * exponent) + 'x'
        return string
