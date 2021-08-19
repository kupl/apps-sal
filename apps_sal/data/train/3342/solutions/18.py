def pattern(n):
    x = 1
    L = []
    while x <= n:
        result = x * str(x)
        x = x + 1
        L.append(result)
    if n < 1:
        pat = ''
    else:
        pat = '\n'.join(L)
    return pat
