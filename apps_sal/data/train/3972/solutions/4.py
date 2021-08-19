import math


def find_next_square(sq):
    input = float(math.sqrt(sq))
    if input % 1 == 0:  # Check input whether it is an integer
        return pow(int(input) + 1, 2)  # Return the next square if sq is a square
    return -1  # Return -1 otherwise
