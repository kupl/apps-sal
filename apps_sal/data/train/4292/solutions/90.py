def string_clean(s):
    res = ''
    for c in s:
        if c not in '0123456789':
            res += c
    return res
