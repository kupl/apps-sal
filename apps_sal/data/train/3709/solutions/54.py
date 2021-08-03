def simple_multiplication(number: int) -> int:
    """Multiplying a given number by eight if it is an even number and by nine otherwise."""
    return number * (8 if number % 2 == 0 else 9)
