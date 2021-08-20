def string_clean(s):
    x = ''
    for i in s:
        if i >= '0' and i <= '9':
            continue
        x += i
    return x
