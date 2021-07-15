def solve(s):
    if len(s) % 2 != 0:
        return -1
    res, k = 0, 0
    for c in s:
        k += 1 if c == '(' else -1
        if k < 0:
            k += 2
            res += 1
    return res + k // 2
