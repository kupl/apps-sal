import math


def get_participants(h):
    return math.ceil((1 + math.sqrt(1 + 8 * h)) / 2)
