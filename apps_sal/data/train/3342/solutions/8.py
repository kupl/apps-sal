def pattern(n):
    return ''.join(list([str(x) * x + '\n' if n > x else str(x) * x for x in range(1, n + 1)]))
