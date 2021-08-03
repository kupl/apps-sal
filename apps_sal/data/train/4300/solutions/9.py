def solve(a, b):
    if not a:
        return 1
    x, c = a[0], 0
    for i in range(len(b)):
        if b[i] == x:
            c += solve(a[1:], b[i + 1:])
    return c
