def pattern(n):
    a = [str(i) for i in range(1, n + 1)]
    return '\n'.join(''.join(a[i:] + a[:i]) for i in range(n))

