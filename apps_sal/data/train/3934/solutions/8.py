def pattern(n):
    return '\n'.join([''.join([str(n - x) for x in range(0, n - y)]) for y in range(0, n)])
