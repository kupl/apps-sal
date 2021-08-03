import math


def length_of_line(array):
   # Good Luck!
   # return math.sqrt(((array[1][0] - array[0][0]) ^ 2 + (array[1][1] - array[0][1]) ^ 2))
    return '%.2f' % math.hypot(array[1][0] - array[0][0], array[1][1] - array[0][1])
