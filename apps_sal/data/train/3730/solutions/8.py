def capitalize(s):
    a = ''
    for (i, v) in enumerate(s):
        a += v.upper() if i % 2 == 0 else v
    return [a, a.swapcase()]
