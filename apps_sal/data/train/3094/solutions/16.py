def sum_array(arr):
    if arr is None or len(arr) == 1:
        return 0
    arr = sorted(arr)
    return sum(arr[1:-1])
