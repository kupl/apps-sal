def sum_array(arr):
    return 0 if type(arr) is not list or len(arr) in (0, 1) else sum(arr) - max(arr) - min(arr)
