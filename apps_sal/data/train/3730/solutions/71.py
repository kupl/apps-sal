def capitalize(s):
    i = 0
    s1 = ''
    s2 = ''
    while i < len(s):
        if i % 2 == 0:
            s1 += s[i].upper()
            s2 += s[i].lower()
        else:
            s1 += s[i].lower()
            s2 += s[i].upper()
        i += 1
    return [s1, s2]
