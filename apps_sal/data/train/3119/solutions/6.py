def pattern(n, y=1, *_):
    if n < 1:
        return ''
    ans, p, y = [], [], max(y, 1)
    for i in range(1, n+1):
        t = [' '] * (n * 2 - 1)
        t[i - 1] = t[n * 2 - 1 - 1 - i + 1] = str(i % 10)
        p.append(''.join(t))
    p += p[:-1][::-1]
    for _ in range(y):
        ans += p[1:] if ans else p
    return '\n'.join(ans)
