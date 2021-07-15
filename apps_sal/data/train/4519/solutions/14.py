def max_number(n: int) -> int:
    """ Return the maximum number that could be formed from the digits of the number given. """
    return int("".join(sorted(str(n), reverse=True)))
