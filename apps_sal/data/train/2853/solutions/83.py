def solve(arr):
    t = []
    for i in range(len(arr)):
        if arr[i:].count(arr[i]) == 1:
            t.append(arr[i])
    return t
