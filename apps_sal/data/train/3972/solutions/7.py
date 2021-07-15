from math import sqrt
def find_next_square(sq):

    if int(sqrt(sq)) == sqrt(sq):
        return (sqrt(sq) + 1) ** 2
    else:
        return -1

