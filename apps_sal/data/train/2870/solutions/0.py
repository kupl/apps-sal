def same(arr_a, arr_b):
    return sorted(map(sorted, arr_a)) == sorted(map(sorted, arr_b))
