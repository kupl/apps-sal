def rotate(arr, n):
    if n > 0:
        n = n % len(arr)
    elif n < 0:
        n = len(arr) - (abs(n) % len(arr))

    arr = arr[-n:] + arr[0:-n]
    return arr
