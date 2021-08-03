def repeat_it(s, n):
    t = s
    if isinstance(s, str) and n != 0:
        for i in range(n - 1):
            s += t
        return s
    if n == 0:
        return ''
    return 'Not a string'
