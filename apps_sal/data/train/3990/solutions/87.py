def derive(coefficient, exponent):
    square = coefficient * exponent
    return f"{square}x^{int(exponent-1)}"
