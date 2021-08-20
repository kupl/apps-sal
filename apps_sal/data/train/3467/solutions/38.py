def integrate(coefficient: int, exponent: int) -> str:
    return str(coefficient // (exponent + 1)) + 'x^' + str(exponent + 1)
