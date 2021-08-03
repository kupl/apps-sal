def pattern(n):
    a = [str(i) for i in range(n, 0, -1)]
    return '\n'.join(''.join(a[:i]) for i in range(1, n + 1))
