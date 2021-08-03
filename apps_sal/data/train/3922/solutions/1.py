def jumping(arr, n):
    i, arr = 0, arr[:]
    arr[0] += 1
    while i < len(arr):
        delta = arr[i]
        arr[i] += (arr[i] < n) - (arr[i] >= n)
        i += delta
    return arr.count(n)
