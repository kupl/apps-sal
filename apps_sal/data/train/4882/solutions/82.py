import math
def round_to_next5(n):
    divide=n/5
    new=math.ceil(divide)
    n=new*5
    return n
