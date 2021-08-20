def pattern(n):
    return '\n'.join((''.join((str(n - j) for j in range(0, n - i + 1))) for i in range(1, n + 1)))
