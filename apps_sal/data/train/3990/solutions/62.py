def derive(coefficient, exponent):
    a = coefficient*exponent
    b = abs(1 - exponent)
    return f"{a}x^{b}"
