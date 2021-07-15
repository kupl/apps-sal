def solve(arr):
    arr.sort()
    res = 1
    for i in range(len(arr)):
        if arr[i] <= res:
            res += arr[i]
    return res
