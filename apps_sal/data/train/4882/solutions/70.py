import string


def round_to_next5(n):
    if ((n % 5) != 0):
        return n + (5 - (n % 5))
    return n
