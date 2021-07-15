def integrate(coefficient, exponent):
    exponent += 1
    coefficient //= exponent
    return f'{coefficient}x^{exponent}'
