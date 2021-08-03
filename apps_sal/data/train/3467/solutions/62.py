def integrate(coefficient, exponent):
    coefficient = int((coefficient / (exponent + 1)))
    exponent += 1
    return ("{0}x^{1}").format(coefficient, exponent)
