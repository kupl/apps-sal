def rotate(arr, n):
    return arr[-n % len(arr):] + arr[:-n % len(arr)]
