import math


def starting_mark(height):
    if height == 1.22:
        return 8.27
    elif height == 2.13:
        return 11.85
    else:
        return round((8.27 + 0.0393444 * ((height - 1.22) * 100)), 2)
