import math

def area(d, l): 
    if l>=d:
        return 'Not a rectangle'
    x = math.sqrt(d*d-l*l)
    a = (x*l)
    return round(a,2)

