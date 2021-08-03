def solve(a, b):
    if len(a) == 1:
        return b.count(a)
    r = 0
    for i in range(len(b) - len(a) + 1):
        if b[i] == a[0]:
            r += solve(a[1:], b[i + 1:])
    return r
