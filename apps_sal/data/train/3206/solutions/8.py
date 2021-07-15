import math
def sum_circles(*args):
    y=  round(sum    ([(math.pi*x**2/4) for x in args]))
    return  "We have this much circle: " +str(y)
