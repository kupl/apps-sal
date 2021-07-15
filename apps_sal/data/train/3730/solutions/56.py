def capitalize(s):
    str1 = ''
    str2 = ''
    for i,c in enumerate(s):
        if not i % 2:
            str1 += c.upper()
            str2 += c.lower()
        else:
            str2 += c.upper()
            str1 += c.lower()
    return [str1, str2]
