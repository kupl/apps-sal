import math


def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
