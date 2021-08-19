def simplify(s):
    a = [i for i in str(s)]
    r = ''
    l = len(a)
    for i in range(len(a)):
        if a[i] == '0':
            continue
        if len(r) > 0:
            r += '+'
        r += a[i]
        if i < len(a) - 1:
            r += '*1' + '0' * (len(a) - i - 1)
    return r
