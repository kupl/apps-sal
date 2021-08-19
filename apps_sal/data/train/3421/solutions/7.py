FIBONACCI = [1, 1]


def mysterious_pattern(m, n):
    while len(FIBONACCI) < m:
        FIBONACCI.append(FIBONACCI[-2] + FIBONACCI[-1])
    pattern = [[' '] * m for _ in range(n)]
    for i in range(m):
        pattern[FIBONACCI[i] % n][i] = 'o'
    return '\n'.join((''.join(row).rstrip() for row in pattern)).strip('\n')
