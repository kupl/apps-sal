def avg_diags(m):
    l = len(m)
    a = [m[i][i] for i in range(1, l, 2) if m[i][i] >= 0]
    b = [m[i][l - i - 1] for i in range(l) if m[i][l - i - 1] < 0 and (l - i - 1) % 2 == 0]
    return [int(round(sum(a) / len(a))) if a else -1, int(round(abs(sum(b)) / len(b))) if b else -1]
