from functools import reduce

def find_smallest_int(arr):
    return reduce(lambda a,b:min(a,b), arr)
