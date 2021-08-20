def bishop_diagonal(a, b):
    (a, b) = sorted([['abcdefgh'.index(f), '12345678'.index(r)] for (f, r) in [a, b]])
    m = int((b[1] - a[1]) / (b[0] - a[0])) if abs(a[1] - b[1]) == abs(a[0] - b[0]) and abs(a[1] - b[1]) else 0
    if m:
        while all((0 < e < 7 for e in a)):
            a = [a[0] - 1, a[1] - m]
        while all((0 < e < 7 for e in b)):
            b = [b[0] + 1, b[1] + m]
    return ['abcdefgh'[c] + '12345678'[r] for (c, r) in [a, b]]
