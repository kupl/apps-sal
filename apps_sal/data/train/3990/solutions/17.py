def derive(coefficient, exponent):
    if ((exponent != 1) and (coefficient != 0) and (exponent != 0)):
        product = coefficient * exponent
        new_exponent = exponent - 1
        return str(product) + "x^" + str(new_exponent)
    else:
        pass
