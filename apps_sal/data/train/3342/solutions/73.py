def pattern(n):
    s = ''
    for i in range(1, n + 1):
        s += ''.join([str(i) for _ in range(i)])
        s += '\n'
    return s[:-1]
