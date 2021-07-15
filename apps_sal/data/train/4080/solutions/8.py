def arr_check(arr):
    return len([el for el in arr if type(el) == list]) == len(arr)
