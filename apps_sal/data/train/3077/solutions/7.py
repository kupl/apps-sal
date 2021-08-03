def pattern(n):
    return '\n'.join([''.join(str(i) for i in range(e, n + 1)) for e in range(1, n + 1)])
