def pattern(n):
    if n < 1:
        return ''
    p = []
    for x in range(1, n + 1):
        p.append(str(x) * x)
    return '\n'.join((str(i) for i in p))
