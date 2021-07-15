def min_sum(arr):
    a = sorted(arr)
    sm = 0
    for i in range(len(arr) // 2):
        sm += a[i] * a[len(a)- i - 1]
    return sm
