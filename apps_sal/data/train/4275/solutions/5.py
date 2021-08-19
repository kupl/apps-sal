def pattern(n):
    return '' if n <= 0 else '\n'.join([str(i) * i for i in range(1, n + 1, 2)])
