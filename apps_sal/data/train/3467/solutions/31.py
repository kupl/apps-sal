def integrate(coefficient, exponent):
    c = 1 + exponent
    newco = int(coefficient / c)
    return f'{newco}x^{c}'
