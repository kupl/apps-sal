def recaman(n):
    seq = {0}
    cur = 0
    for i in range(1, n + 1):
        cur += [i, -i][cur - i not in seq and cur - i > 0]
        seq.add(cur)
    return cur
