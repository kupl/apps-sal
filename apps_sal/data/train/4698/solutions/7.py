def is_int_array(arr):
    return isinstance(arr, list) and all(map(lambda x: isinstance(x, (int, float)) and int(x) == x, arr))
