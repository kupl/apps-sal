from operator import mul    
from functools import reduce
def select_subarray(array):
    l = []
    for i in array:
        arr = [j for j in array if j != i]
        if sum(arr):
            l.append(((abs(reduce(mul, arr)/float(sum(arr)))), array.index(i), i))
    c = [[j, k] for i, j, k in l if i == sorted(l)[0][0]]
    return c[0] if len(c) == 1 else c

