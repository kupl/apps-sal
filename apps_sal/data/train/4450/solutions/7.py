def consecutive(arr):
    arr = sorted(arr)
    return arr[-1] - arr[0] - len(arr[1:]) if len(arr) > 0 else 0
