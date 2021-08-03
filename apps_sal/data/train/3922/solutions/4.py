def jumping(arr, n):
    c = 0
    while c < len(arr):
        T = arr[c] // 1
        c += T
        arr[c - T] += -1 if arr[c - T] >= n else 1
    return arr.count(n)
