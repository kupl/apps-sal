def solve(st, k):
    x = len(st) - k
    m = 0
    for i in range(len(str(st))):
        y = int(st[i:i + x])
        if y > m:
            m = y
    return m
