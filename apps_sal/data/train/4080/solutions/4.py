def arr_check(arr):
    return all(type(i) is list for i in arr)
