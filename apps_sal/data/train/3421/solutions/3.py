def mysterious_pattern(m, n):
    (lines, a, b) = ([[' '] * m for _ in range(n)], 1, 1)
    for i in range(m):
        (lines[a % n][i], a, b) = ('o', b, a + b)
    return '\n'.join([''.join(l).rstrip() for l in lines]).strip('\n')
