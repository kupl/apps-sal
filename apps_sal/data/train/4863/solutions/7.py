def circularly_sorted(arr):
    while arr[-1] <= arr[0]:
        arr = [arr.pop()] + arr
    return arr == sorted(arr)
