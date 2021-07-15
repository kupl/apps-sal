import math
def is_divisible(n,x,y):
    return math.floor(n/x)==math.ceil(n/x) and math.floor(n/y)==math.ceil(n/y)
