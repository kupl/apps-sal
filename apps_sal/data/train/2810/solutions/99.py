def solve(arr):
    res = []
    for i in arr:
        tmp = 0
        for e, j in enumerate(i.lower()):
            if chr(e + 97) == j:
                tmp += 1
        res.append(tmp)
    return res
