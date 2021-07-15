import math


def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise"""
    square = math.sqrt(float(sq))
    return -1 if not square.is_integer() else math.pow(square + 1, 2)

