def integrate(coefficient, exponent):
    exponent += 1
    coefficient /= exponent
    coefficient = (int if coefficient.is_integer() else float)(coefficient)
    return f'{coefficient}x^{exponent}'
