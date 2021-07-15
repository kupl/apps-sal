import numpy as np

def find_dups_miss(arr):
    arr=sorted(arr)
    diff=np.array(arr[1:])-np.array(arr[:-1])
    rep = [ arr[i] for i, x in enumerate(diff) if x == 0 ]
    unico=[ arr[i]+1 for i, x in enumerate(diff) if x == 2 ]
    return [unico[0],rep]
