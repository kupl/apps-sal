import math
def length_of_line(array):
  return "{:.02f}".format(math.sqrt((array[1][0] - array[0][0])**2 + (array[1][1] - array[0][1])**2))

