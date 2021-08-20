def avg_diags(m):
    (a1, a2, l, l1, l2) = (0, 0, len(m), 0, 0)
    for i in range(0, l):
        if i & 1:
            if m[i][i] >= 0:
                a1 += m[i][i]
                l1 += 1
        elif m[l - i - 1][i] < 0:
            a2 += m[len(m) - i - 1][i]
            l2 += 1
    return [round(a1 / l1) if l1 > 0 else -1, round(abs(a2) / l2) if l2 > 0 else -1]
