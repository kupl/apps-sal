def around_fib(n):
    f = str(fib(n))
    ch = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    maxcnt = 0
    chunk = ''

    for digit in ch:
        cnt = f.count(digit)
        if cnt >= maxcnt:
            maxcnt = cnt
            maxdig = digit

    l = len(f) % 25
    if l == 0:
        start = len(f) - 25
    else:
        start = len(f) - l
    for i in range(start, len(f)):
        chunk += f[i]

    return 'Last chunk ' + chunk + '; Max is %d for digit ' % maxcnt + maxdig


def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
