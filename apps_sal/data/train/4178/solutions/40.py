def min_sum(arr):
    summ = 0
    arr = sorted(arr)
    for i in range(len(arr)):
        summ += arr[i] * arr[len(arr) - 1 - i]
    return summ / 2
