def pattern(n):
    return '\n'.join(x * str(x) for x in range(1, n + 1)) if n > 0 else ''
