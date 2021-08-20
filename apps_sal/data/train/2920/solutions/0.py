def pattern(n):
    return '\n'.join((''.join((str(i) for i in range(n, j, -1))) for j in range(n - 1, -1, -1)))
