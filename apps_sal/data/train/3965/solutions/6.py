import math


def powerof4(n):
    if not (isinstance(n, int) and not isinstance(n, bool) and n > 0):
        return False
    return math.log(n, 4).is_integer()

