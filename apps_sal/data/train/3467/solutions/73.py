def integrate(coefficient, exponent):
    exponent = exponent + 1
    coefficient = coefficient / exponent if coefficient % exponent else coefficient // exponent
    return f'{coefficient}x^{exponent}'
    


