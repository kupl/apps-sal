def capitalize(s):
    p = len(s)
    newar = []
    o = ""
    e = ""
    for i in range(0, p):
        if i & 1:
            e += s[i].upper()
            o += s[i]
        else:
            e += s[i]
            o += s[i].upper()
    newar.append(o)
    newar.append(e)
    return newar
