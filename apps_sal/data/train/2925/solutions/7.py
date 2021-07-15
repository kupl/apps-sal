def multiply(n: int) -> int:
    """ Multiply each number by 5 raised to the number of digits of each numbers. """
    return n * pow(5, len(str(abs(n))))
