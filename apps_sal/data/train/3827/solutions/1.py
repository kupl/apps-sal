from math import asin, acos, atan, degrees as d
missing_angle=lambda h,a,o:round(d(atan(o/a) if not h else asin(o/h) if not a else acos(a/h)))
