def string_clean(s):
    n = ''
    for i in range(0, len(s)):
        if s[i].isdigit():
            continue
        else:
            n = n + s[i]
    return n
