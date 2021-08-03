def how_many_bees(hive):
    if not hive:
        return 0
    r = 0
    for row in hive:
        r += ''.join(row).count('bee')
        r += ''.join(row[::-1]).count('bee')
    for column in zip(*hive):
        r += ''.join(column).count('bee')
        r += ''.join(column[::-1]).count('bee')
    m, n = len(hive), len(hive[0])
    for i in range(m):
        for j in range(n):
            if hive[i][j] == 'b':
                if i < m - 2 and j < n - 2:
                    if hive[i + 1][j + 1] == hive[i + 2][j + 2] == 'e':
                        r += 1
                if i < m - 2 and j >= 2:
                    if hive[i + 1][j - 1] == hive[i + 2][j - 2] == 'e':
                        r += 1
                if i >= 2 and j < n - 2:
                    if hive[i - 1][j + 1] == hive[i - 2][j + 2] == 'e':
                        r += 1
                if i >= 2 and j >= 2:
                    if hive[i - 1][j - 1] == hive[i - 2][j - 2] == 'e':
                        r += 1
    return r
