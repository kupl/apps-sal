import math

def area ( diagonal, side ):
    if diagonal <= side: return 'Not a rectangle'
    
    return round(math.sqrt(diagonal ** 2 - side ** 2) * side, 2)
