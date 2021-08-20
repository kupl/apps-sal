def capitalize(s):
    lst = []
    print(s)
    (a, b) = ('', '')
    for i in range(len(s)):
        if i % 2 == 0 or i == 0:
            a = a + s[i].upper()
        else:
            a = a + s[i]
    for i in range(len(s)):
        if i % 2 != 0:
            b = b + s[i].upper()
        else:
            b = b + s[i]
    lst.append(a)
    lst.append(b)
    return lst
