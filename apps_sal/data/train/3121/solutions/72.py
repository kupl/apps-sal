def solve(arr):
    parr = []
    narr = []
    for i in arr:
        if i < 0:
            narr.append(i)
        else:
            parr.append(i)
    res = 0
    for a in narr:
        if abs(a) not in parr:
            res = a
    for b in parr:
        if b*-1 not in narr:
            res = b
    return res

