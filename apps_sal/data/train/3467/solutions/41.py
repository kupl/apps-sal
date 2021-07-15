def integrate(coefficient, exponent):
    a = exponent + 1
    b = round(coefficient / a)
    return f"{b}x^{a}"
