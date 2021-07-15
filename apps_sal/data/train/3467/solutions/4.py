def integrate(coefficient, exponent):
    exponent += 1
    coefficient /= exponent
    return '{}x^{}'.format(int(coefficient) if coefficient.is_integer() else coefficient, exponent)
