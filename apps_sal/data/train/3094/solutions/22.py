def sum_array(arr):
    if arr == None:
        return 0
    return sum(sorted(arr)[1:-1]) if len(arr) > 2 else 0
