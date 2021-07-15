def mysterious_pattern(m, n):
    rows = [[' '] * m for _ in range(n)]
    a, b = 1, 1
    for i in range(m):
        rows[a % n][i] = 'o'
        a, b = b, a + b
    rows = [''.join(r).rstrip() for r in rows]
    return '\n'.join(rows).strip('\n')
