def pattern(n):
    s = ''.join((str(x % 10) for x in reversed(range(1, n + 1))))
    return '\n'.join((s[:x + 1] + s[x] * (n - x - 1) for x in range(n)))
