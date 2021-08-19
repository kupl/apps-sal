def integrate(coefficient, exponent):
    new_exp = exponent + 1
    new_coef = int(coefficient / new_exp)
    return f'{new_coef}x^{new_exp}'
