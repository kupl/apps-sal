def derive(coefficient, exponent):
    return f'{coefficient*exponent}x' if exponent == 2 else f'{coefficient*exponent}x^{exponent-1}'
