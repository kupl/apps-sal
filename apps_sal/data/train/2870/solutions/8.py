def same(arr_a, arr_b):
    return sorted(sorted(arr) for arr in arr_a) == sorted(sorted(arr) for arr in arr_b)

