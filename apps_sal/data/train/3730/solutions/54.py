def capitalize(s):
    a = ''
    b = ''
    for i in range(len(s)):
        if i % 2 != 1:
            a = a + s[i].upper()
            b = b + s[i]
        else:
            a = a + s[i]
            b = b + s[i].upper()
    return [a, b]
    pass
