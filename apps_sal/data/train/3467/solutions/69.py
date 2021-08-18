def integrate(coefficient, exponent):
    aa = int(coefficient / (exponent + 1))
    bb = exponent + 1
    return (f"{aa}x^{bb}")
