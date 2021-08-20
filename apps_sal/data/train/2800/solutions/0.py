from math import sin, radians


def find_time_to_break(bearing_A, bearing_B):
    a = radians(abs(bearing_A - bearing_B) / 2)
    return 40 / (3 * sin(a)) if a else float('inf')
