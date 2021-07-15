import numpy as np
def nth_smallest(arr, pos):
    res=np.sort(arr)
    d=res[pos-1]
    
    return d

