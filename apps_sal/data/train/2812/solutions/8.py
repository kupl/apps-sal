def pattern(n):
    return '\n'.join((i * str(i) for i in range(2, n + 1, 2)))
