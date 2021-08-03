def jumping(arr, n):
    i = 0
    print(arr)
    while i < len(arr):
        k = arr[i]
        if k >= n:
            arr[i] -= 1
        elif k < n:
            arr[i] += 1
        i += k
    return sum([i == n for i in arr])
