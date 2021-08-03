def around_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    f = str(a)
    start = (len(f) - 1) // 25 * 25
    maxcnt, ch = min((-f.count(d), d) for d in '0123456789')
    return "Last chunk %s; Max is %d for digit %s" % (f[start:], -maxcnt, ch)
