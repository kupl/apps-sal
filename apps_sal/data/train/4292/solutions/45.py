def string_clean(s):
    toremove = '1234567890'
    for i in s:
        if i in toremove:
            s = s.replace(i, '')
    return s
