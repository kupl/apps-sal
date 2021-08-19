def circularly_sorted(arr):
    m = arr.index(min(arr))
    return sorted(arr) == arr[m:] + arr[:m]
