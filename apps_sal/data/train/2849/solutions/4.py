def peak(arr):
    r = sum(arr) - arr[0]
    l = 0
    if l == r:
        return 0
    for i in range(len(arr) - 1):
        l += arr[i]
        r -= arr[i + 1]
        if l == r:
            return i + 1
    return -1
