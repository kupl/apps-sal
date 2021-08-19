def pattern(n):
    return '\n'.join((str(d) * d for d in range(1, n + 1)))
