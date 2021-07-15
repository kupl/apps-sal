def sum_array(arr):
    if hasattr(arr, 'sort'):
        arr.sort()
        return sum(arr[1:-1], 0)
    else:
        return 0
