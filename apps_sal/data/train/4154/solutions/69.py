import math
def is_triangle(a, b, c):
    sides=(a,b,c)
    if sorted(sides)[-1]>=(sorted(sides)[0]+sorted(sides)[1]):
        return False
    return True

