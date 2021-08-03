from math import asin, acos, atan, degrees as d
def missing_angle(h, a, o): return round(d(atan(o / a) if not h else asin(o / h) if not a else acos(a / h)))
