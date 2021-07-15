import math

def index(array, n):
    for i in range(len(array)):
        if i == n:
            return array[i] ** n
    return -1
