import math
def starting_mark(height):
    k = (10.67 - 9.45) / (1.83 - 1.52)
    b = 9.45 - k * 1.52
    y = k * height + b
    return round(y, 2)
