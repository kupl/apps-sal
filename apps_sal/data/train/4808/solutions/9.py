def equalize(arr):
    return ['+' + str(x - arr[0]) if x >= arr[0] else '-' + str(arr[0] - x) for x in arr]
