def min_sum(arr):
    sum = 0
    a = sorted(arr)
    b = sorted(arr, reverse=True)
    for x in range(len(arr) // 2):
        sum += a[x] * b[x]
    return sum
