def string_clean(s):
    for el in '0123456789':
        s = s.replace(el, '')
    return s
