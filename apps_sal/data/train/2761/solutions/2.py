from math import sqrt

def length_of_line(array):
    (x1, y1), (x2, y2) = array[0], array[1]
    return '{:.2f}'.format(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
