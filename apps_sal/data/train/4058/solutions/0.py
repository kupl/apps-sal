def pattern(n):
    res = []
    for i in range(1, n + 1):
        line = ' ' * (i - 1) + str(i % 10) + ' ' * (n - i)
        res.append(line + line[::-1][1:])
    return '\n'.join(res + res[::-1][1:])
