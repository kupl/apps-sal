def pairwise(arr, n):
    result = 0
    for i in range(len(arr)):
        d = n - arr[i]
        if d in arr[i + 1:]:
            j = arr.index(d, i + 1)
            result += i + j
            arr[i] = arr[j] = n + 1
    return result
