def pattern(n):
    r = range(n, 0, -1)
    a = [str(i) for i in r]
    return '\n'.join(''.join(a[:i]) for i in r)

