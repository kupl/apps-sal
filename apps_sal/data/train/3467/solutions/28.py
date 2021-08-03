def integrate(coefficient, exponent):
    b = exponent + 1
    a = coefficient // b

    return f"{a}x^{b}"
