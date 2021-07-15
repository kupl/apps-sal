def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    else:
        arr.sort()
        return sum(arr) - arr[0] - arr[-1]
