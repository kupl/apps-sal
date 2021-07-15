def integrate(coefficient: int, exponent: int) -> str:
    """ Get the integral of the expression passed. """
    return f"{int(coefficient / (exponent + 1))}x^{exponent + 1}"
