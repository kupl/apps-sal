import math
def index(array, n):
    if len(array) > n:
        return math.pow(array[n], n)
    else:
        return -1
