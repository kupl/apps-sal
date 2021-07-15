def sum_array(arr):
    return 0 if arr is None or len(arr) in [0, 1] else sum(arr) - min(arr) - max(arr)
