def integrate(coefficient, exponent):
    exponent += 1
    num = int(coefficient / exponent)
    return f'{num}x^{exponent}'
