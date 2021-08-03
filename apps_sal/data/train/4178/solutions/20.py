def min_sum(arr):
    ret = 0
    arr = sorted(arr)
    while arr:
        ret += (arr.pop(0) * arr.pop(-1))
    return ret
