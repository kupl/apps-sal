from math import cos, hypot, radians, sin

def find_time_to_break(a, b):
    a, b = radians(a), radians(b)
    d = hypot(cos(a) - cos(b), sin(a) - sin(b))
    return 40 / (90 / 60) / d if d else float('inf')
