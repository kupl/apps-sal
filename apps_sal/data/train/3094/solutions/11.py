def sum_array(arr):
    return 0 if arr is None else sum(sorted(arr)[1:-1])
