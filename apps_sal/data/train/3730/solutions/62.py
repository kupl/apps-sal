def capitalize(s):
    l = []
    x = ""
    for i in range(len(s)):
        if i % 2 == 0:
            j = s[i].capitalize()
            x += j
        else:
            x += s[i]
    w = ""
    for i in range(len(s)):
        if not i % 2 == 0:
            k = s[i].capitalize()
            w += k
        else:
            w += s[i]
    l.append(x)
    l.append(w)
    return l
