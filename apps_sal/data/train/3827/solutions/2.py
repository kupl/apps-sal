import math

def missing_angle(h, a, o):
    return round(math.degrees(math.atan(o/a) if not h else math.asin(o/h) if not a else math.acos(a/h)))
