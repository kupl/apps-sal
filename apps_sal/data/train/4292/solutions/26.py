def string_clean(s):
    res = ''
    for i in range(len(s)):
        if not s[i].isdigit():
            res += (s[i])
    return res
