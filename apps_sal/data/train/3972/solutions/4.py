import math


def find_next_square(sq):
    input = float(math.sqrt(sq))
    if input % 1 == 0:
        return pow(int(input) + 1, 2)
    return -1
