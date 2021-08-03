def pattern(n):
    s = ''.join(str((i if i < n else n if i < n * 2 else (n * 3) - i - 1) % 10) for i in range(1, n * 3 - 1))
    return '\n'.join((s[i] * n).center(n * 3 - 2) if i < n - 1 or i >= n * 2 - 1 else s for i in range(n * 3 - 2))
