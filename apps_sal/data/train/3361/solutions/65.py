def sum_of_minimums(arr):
    mx = 0
    for i in range(len(arr)):
        mn = min(arr[i])
        mx += mn
    return mx
