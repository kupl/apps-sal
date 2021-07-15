def derive(coefficient: int, exponent: int) -> str:
    """ Multiply the two numbers and then subtract 1 from the exponent. """
    return f"{coefficient * exponent}x^{exponent - 1}" if exponent > 2 else f"^{exponent - 1}"
