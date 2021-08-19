def string_clean(s):
    n = '1234567890'
    for x in n:
        if x in s:
            s = s.replace(x, '')
    return s
