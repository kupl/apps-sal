def pattern(n):
    res = [str(i) * i for i in range(1, n + 1)]
    return '\n'.join(res)
