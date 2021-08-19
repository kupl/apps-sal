def avg_diags(m):
    (a, ac, b, bc, n) = (0, 0, 0, 0, len(m))
    for i in range(n):
        if i & 1 == 1 and m[i][i] >= 0:
            a += m[i][i]
            ac += 1
        if n - i - 1 & 1 == 0 and m[i][n - i - 1] < 0:
            b += m[i][n - i - 1]
            bc += 1
    return [-1 if ac == 0 else round(a / ac), -1 if bc == 0 else round(abs(b / bc))]
