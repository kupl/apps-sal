def string_clean(s):
    lsValue = ''
    for i in range(len(s)):
        if not s[i].isnumeric():
            lsValue += s[i]
    return lsValue
