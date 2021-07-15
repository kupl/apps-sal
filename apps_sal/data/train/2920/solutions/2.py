def pattern(n):
    full = [str(x) for x in range(n, 0, -1)]
    take = lambda x: ''.join(full[:x])
    return '\n'.join((take(x) for x in range(1, n + 1)))
