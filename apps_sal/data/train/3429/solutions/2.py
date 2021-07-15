from math import pi
def circleArea(r):
    if type(r) == int and r>0:
        return round(pi*(r**2), 2)
    else:
        return False

