import math
from functools import reduce
import operator

def select_subarray(arr):
    q_vals = []
    for i in range(len(arr)):
        a = arr[:i] + arr[i+1:]
        sum_a = sum(a)
        if sum_a == 0:
            q_vals.append(None)
        else:
            q_vals.append(math.fabs(reduce(operator.mul, a, 1) / sum_a))
    selected = min(filter(lambda x: x is not None, q_vals))
    indexes = [i for i,x in enumerate(q_vals) if x==selected]
    result = []
    for index in indexes:
        result.append([index,arr[index]])
    if len(result)==1:
        return result[0]
    return result
