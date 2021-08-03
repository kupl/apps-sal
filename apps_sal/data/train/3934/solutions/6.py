def pattern(n):
    return '\n'.join([''.join([str(n - y) for y in range(n - x + 1)]) for x in range(1, n + 1)])
