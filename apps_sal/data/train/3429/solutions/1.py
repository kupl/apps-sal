import math

def circleArea(r):
    try:
        if (r > 0):
            return round(math.pi*r**2, 2)
        else:
            return False
    except TypeError:
        return False

