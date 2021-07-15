from math import cos, radians, inf

def find_time_to_break(bearing_A, bearing_B):
    theta = bearing_A - bearing_B
    return inf if theta == 0 else 18.86 / (1 - cos(radians(theta)))**0.5
