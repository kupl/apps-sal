from math import floor
def sum_average(arr):
    return floor(sum(sum_average(x)/len(x) if type(x) is list else x for x in arr))
