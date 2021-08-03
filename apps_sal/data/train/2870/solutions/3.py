def same(arr_a, arr_b):
    return sorted(sorted(x) for x in arr_a) == sorted(sorted(x) for x in arr_b)
