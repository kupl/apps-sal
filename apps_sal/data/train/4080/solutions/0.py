def arr_check(arr):
    return all(isinstance(el, list) for el in arr)
