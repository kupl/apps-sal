def sum_array(arr):
    return 0 if not arr or len(arr) <= 2 else sum(arr) - max(arr) - min(arr)
