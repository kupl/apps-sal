from math import log

def power_law(x1y1, x2y2, x3):
    a, b, c = x2y2[0]/x1y1[0], x2y2[1]/x1y1[1], x3/x1y1[0]
    try:
         return round(x1y1[1] * b**log(c, a))
    except ZeroDivisionError:
         return round(x1y1[1] * b)
