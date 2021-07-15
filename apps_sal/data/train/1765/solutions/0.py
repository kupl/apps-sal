def partitions(n):
    c = [[1]]
    for x in range(1, n + 1):
        c.append([0])
        for m in range(1, x + 1):
            c[x].append(c[x][m - 1] + c[x - m][min(m, x - m)])
    return c[n][n]
