def pattern(n):
    return '\n'.join([str(r) * r for r in range(1, n + 1)])
