def capitalize(s):
    a1 = a2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            a1 += s[i].upper()
            a2 += s[i]
        else:
            a2 += s[i].upper()
            a1 += s[i]
    return [a1, a2]
