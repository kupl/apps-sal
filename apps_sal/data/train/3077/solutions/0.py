def pattern(n):
    return '\n'.join([''.join([str(y) for y in range(x + 1, n + 1)]) for x in range(n)])
