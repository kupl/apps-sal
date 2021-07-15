def sum_array(arr):
    return 0 if arr == None or len(arr) < 2 else sum(arr) - min(arr) - max(arr)

