import math
def new_avg(arr, newavg):
    result =  math.ceil(newavg*(len(arr)+1)-sum(arr))    
    if result <= 0:
        raise ValueError('error')
    else:
        return result
