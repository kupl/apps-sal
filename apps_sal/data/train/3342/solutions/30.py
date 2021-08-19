def pattern(n):
    return '\n'.join((str(n) * n for n in range(1, n + 1))) if n > 0 else ''
