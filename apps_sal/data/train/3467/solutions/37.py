def integrate(coefficient: int, exponent: int) -> str:
    """ Get the integral of the expression passed. """
    return f"{coefficient / (exponent + 1):.0f}x^{exponent + 1}"
