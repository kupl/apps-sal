def arr_check(arr):
    return sum([isinstance(x, list) for x in arr]) == len(arr)
