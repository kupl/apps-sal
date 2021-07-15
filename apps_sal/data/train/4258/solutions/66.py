import math
def series_sum(n):
    # Happy Coding ^_^
    result = 0.00
    for i in (list(range(0, n))): 
        result += 1.00 / (1.00 + (3.00 * float(i)) )
    return "{:.2f}".format(result)
    
    

