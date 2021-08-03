def avg_diags(m):
    r1 = [m[i][i] for i in range(1, len(m), 2) if m[i][i] >= 0]
    r2 = [m[-i - 1][i] for i in range(0, len(m), 2) if m[-i - 1][i] <= 0]
    return [round(sum(r1) / len(r1)) if r1 else -1, abs(round(sum(r2) / len(r2))) if r2 else -1]
