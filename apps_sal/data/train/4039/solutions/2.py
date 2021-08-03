def fouriest(i):
    b = 4
    m = 0
    l = i
    B = b
    while m < l:
        b += 1
        f, x, l = base(i, b)
        if f > m:
            m = f
            N = x
            B = b
    return "%d is the fouriest (%s) in base %d" % (i, N, B)


def base(n, b):
    f = 0
    s = ''
    while n:
        x = n % b
        s = (str(x)if x < 10 else 'x') + s
        n //= b
    return s.count('4'), s, len(s)
