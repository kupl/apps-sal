def solve(arr):
    s = []
    for k, v in enumerate(arr):
        if arr[k + 1:].count(v) == 0:
            s.append(arr[k])
    return s
