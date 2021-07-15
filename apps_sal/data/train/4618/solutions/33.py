from functools import reduce
def positive_sum(arr):
    return reduce(lambda x,y: x+max(0,y), arr, 0)
