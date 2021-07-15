def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(e, int) or isinstance(e, float) and e.is_integer() for e in arr)
