def replace_dots(s):
    s = list(s)
    i = 0
    while i < len(s):
        if s[i] == '.':
            s[i] = '-'
        i += 1
    return ''.join(s)
