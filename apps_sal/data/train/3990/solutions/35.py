def derive(coefficient, exponent): 
    return f'{coefficient * exponent}x^{exponent - 1}' if exponent > 1 else f'{coefficient * exponent}x'
