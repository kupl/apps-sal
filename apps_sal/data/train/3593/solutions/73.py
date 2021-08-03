def capitalize(s, ind):
    out = ""
    s = list(s)
    for i in ind:
        if i < len(s):
            s[i] = s[i].upper()
    return "".join(s)
