def pattern(n):
    pat = ''
    for i in range(1, n + 1):
        pat += i * str(i) + '\n'
    return pat[:-1]
