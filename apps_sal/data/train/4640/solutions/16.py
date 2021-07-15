def int_diff(arr, n):
    arr.sort()
    return sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[j] - arr [i] == n)

