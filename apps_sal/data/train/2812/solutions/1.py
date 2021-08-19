def pattern(n):
    return '\n'.join((str(i) * i for i in range(2, n + 1, 2)))
