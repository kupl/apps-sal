def pattern(n, y=1, *args):
    p = [''.join([' ' * (i - 1), str(i % 10), ' ' * (n - i)]) for i in range(1, n + 1)]
    p = [''.join([i, i[-2::-1]]) for i in p]
    p += p[-2::-1]
    return '\n'.join(p + p[1:] * (y - 1))
