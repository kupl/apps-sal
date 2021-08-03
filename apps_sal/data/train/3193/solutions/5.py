def stairs(n):
    l, s = [], []
    for i in range(1, n + 1):
        l.append(str(i % 10))
        s.append(' '.join(l + l[::-1]))
    return '\n'.join(r.rjust(len(s[-1])) for r in s)
