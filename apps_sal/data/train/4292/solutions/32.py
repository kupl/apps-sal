def string_clean(s):
    for c in '1234567890':
        s = s.replace(c, '')
    return s
