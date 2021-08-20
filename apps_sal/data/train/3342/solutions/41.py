def pattern(n):
    return '\n'.join((str(loop) * loop for loop in range(1, n + 1)))
