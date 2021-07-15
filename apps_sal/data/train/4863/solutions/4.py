def circularly_sorted(arr):
    i = len(arr) - arr[::-1].index(min(arr)) - 1
    return arr[i:] + arr[:i] == sorted(arr)
