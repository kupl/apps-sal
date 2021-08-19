def base(n, b):
    a = '0123456789abcdef'
    r = ''
    while n:
        (n, i) = divmod(n, b)
        r = a[i] + r
    return r or '0'


def func(l):
    n = sum(l) // len(l)
    return [n, base(n, 2), base(n, 8), base(n, 16)]
