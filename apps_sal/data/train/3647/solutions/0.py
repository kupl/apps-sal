def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res
