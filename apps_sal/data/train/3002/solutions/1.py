import math


def is_pronic(n):
    """Return True if given number is pronic, else False."""
    if n == 0:
        return True
    if n < 0:
        return False
    first_int = int(math.sqrt(n))
    second_int = first_int + 1
    return first_int * second_int == n
