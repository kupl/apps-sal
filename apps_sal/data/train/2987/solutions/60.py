def is_divide_by(number: int, a: int, b: int) -> bool:
    """
    check is number is divisble by both a and b
    """
    return True if number % a is 0 and number % b is 0 else False
