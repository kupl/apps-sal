from math import (sin, radians)


def find_time_to_break(b1, b2):
    return round(40 / sin(radians(abs(b1 - b2)) / 2) / 3, 2) if b1 - b2 != 0 else float("inf")
