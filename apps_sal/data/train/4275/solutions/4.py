def pattern(n):
    x = []
    if n <= 0:
        return ''
    else:
        for a in range(1, n + 1, 2):
            x.append(str(a) * a)
    return '\n'.join(x)
