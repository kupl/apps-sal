def x(n):
    i = 0
    out = ''
    while i < n:
        out = out + line(n, i)
        if i != (n - 1):
            out = out + '\n'
        i = i + 1
    return out


def line(x, ln):
    blank = '□'
    pixel = '■'
    str = ''
    n = 0
    while n < x:
        if n == ln:
            str = str + pixel
        elif n == ((x - 1) - ln):
            str = str + pixel
        else:
            str = str + blank
        n = n + 1
    return str
