def solve(arr):
    res = []
    for v in arr[-1::-1]:
        if v not in res:
            res.append(v)
    return res[-1::-1]
