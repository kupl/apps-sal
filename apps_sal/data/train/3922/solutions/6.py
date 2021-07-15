def jumping(arr, n):
    i = 0
    while i < len(arr):
        t = arr[i]
        arr[i] += 1 if t < n else -1
        i += t
    return arr.count(n)
