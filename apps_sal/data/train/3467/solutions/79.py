def integrate(coefficient, exponent):
    new_coefficient = str(coefficient // (exponent + 1))
    new_exponent = str(exponent + 1)
    return f'{new_coefficient}x^{new_exponent}'
