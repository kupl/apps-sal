import numpy as np
def min_unfairness(arr,k):
    arr=np.sort(np.array(arr))
    if arr.size<2 or k in (0,1):
        return 0
    return np.min(arr[k-1:]-arr[:-k+1])
