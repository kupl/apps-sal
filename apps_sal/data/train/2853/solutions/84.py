def solve(arr):
    res = []
    for i in arr[::-1]:
        if i in res:
            continue
        else:
            res.insert(0, i)
    return res
