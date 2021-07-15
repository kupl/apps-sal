def same(arr_a, arr_b):
    arr_a = sorted(list(map(sorted, arr_a)))
    arr_b = sorted(list(map(sorted, arr_b)))
    return arr_a == arr_b
