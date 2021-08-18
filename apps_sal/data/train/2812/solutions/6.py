def pattern(n):
    return '\n'.join([str(a) * a for a in range(2, n + 1, 2)])
