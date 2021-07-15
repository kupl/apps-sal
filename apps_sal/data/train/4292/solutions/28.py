def string_clean(s):
    num = '0123456789'
    for i in s:
        if i in num:
            s = s.replace(i, '')
    return s
