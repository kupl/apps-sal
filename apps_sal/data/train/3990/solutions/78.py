def derive(coefficient, exponent):
    coeff_der = coefficient * exponent
    exp_der = exponent - 1
    return "{}x^{}".format(coeff_der, exp_der)
