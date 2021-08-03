def solve(arr):
    arr = sorted(arr)
    l = len(arr)
    x = 1
    for i in range(l):
        if arr[i] <= x:
            x += arr[i]
        else:
            break
    return x
