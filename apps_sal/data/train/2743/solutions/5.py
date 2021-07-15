import numpy as np

def sum_average(arr):
    nm = int(sum([np.mean(arr[i]) for i in range(len(arr)) ]))
    return nm-1 if nm<0 else nm
