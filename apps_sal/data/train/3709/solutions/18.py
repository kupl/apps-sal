def simple_multiplication(number: int) -> int:
    """ Multiply a given number by eight if it is an even number and by nine otherwise. """
    return number * 9 if number % 2 else number * 8
