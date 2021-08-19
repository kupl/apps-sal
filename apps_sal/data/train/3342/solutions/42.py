def pattern(n):
    return ''.join([str(x) * x + '\n' if x < n else str(x) * x for x in range(1, n + 1)])
