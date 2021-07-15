#divide the gris intro two
#the odd grid (has values odd*odd)
#the even grid (has values even*even)
#then add them together

from math import sqrt

def rectangle_rotation(a, b):
    d = sqrt(2)

    #always odd numbers
    x1 = int(a / (2*d)) * 2 +1
    y1 = int(b / (2*d)) * 2 +1
    
    #always even numbers
    x2 = 2* (1 + int(a/(2*d) - (1/2)))
    y2 = 2* (1 + int(b/(2*d) - (1/2)))

    return((x1*y1) + (x2*y2))
