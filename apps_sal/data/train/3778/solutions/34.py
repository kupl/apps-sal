import math
def find_smallest_int(arr):
    x = math.inf
    for i in arr:
        if i < x:
            x = i
    return x
