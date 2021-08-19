def pattern(n):
    return '\n'.join((''.join(map(str, range(n, stop, -1))) for stop in range(n)))
