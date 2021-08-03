def pairs(ar):
    res = 0
    for i in range(1, len(ar), 2):
        if abs(ar[i] - ar[i - 1]) == 1:
            res += 1
    return res
