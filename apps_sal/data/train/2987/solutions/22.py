def is_divide_by(number: int, a: int, b: int) -> bool:
    """ Check if an integer number is divisible by each out of two arguments. """
    return list(map(lambda _divider: number % _divider, [a, b])) == [0, 0]
