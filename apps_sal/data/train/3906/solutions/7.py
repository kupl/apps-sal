def total(arr):
    a = arr[:]
    for i in range(len(a), 1, -1):
        for j in range(1, i):
            a[j - 1] += a[j]
    return a[0]
