def string_clean(s):
    res = ''
    for i in s:
        if i.isdigit():
            continue
        else:
            res += i
    return res
