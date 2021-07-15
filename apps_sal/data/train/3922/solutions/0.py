def jumping(arr, n):
    i = 0
    while i < len(arr):
        x = arr[i]
        arr[i] += 1 if x < n else -1
        i += x
    return arr.count(n)
