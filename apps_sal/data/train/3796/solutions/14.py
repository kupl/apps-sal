def ind(arr, i, default):
    return default if len(arr) - 1 < i else arr[i]

def or_arrays(arr1, arr2, default=0):
    return [ind(arr1, i, default) | ind(arr2, i, default) for i in range(max(len(arr1), len(arr2)))]
