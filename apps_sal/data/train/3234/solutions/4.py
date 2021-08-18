import operator
from functools import reduce


def min_in_dict(in_dict, original_arr):
    positions = []
    min_value = float("inf")
    for key, val in in_dict.items():
        if val == min_value:
            positions.append([original_arr.index(key), key])
        if val < min_value:
            min_value = val
            positions = []
            positions.append([original_arr.index(key), key])
    return positions


def select_subarray(arr):
    q = dict()
    for el in arr:
        temp = arr.copy()
        temp.remove(el)
        if (sum(temp)):
            q[el] = abs(reduce(operator.mul, temp, 1) / sum(temp))
    if (len(min_in_dict(q, arr)) == 1):
        return min_in_dict(q, arr)[0]
    else:
        return min_in_dict(q, arr)
