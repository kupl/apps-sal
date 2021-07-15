import math
def starting_mark(height):
    constant = (10.67 -9.45)/(1.83-1.52)
    return round((constant*height +10.67 -constant*1.83),2)
