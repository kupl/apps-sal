def capitalize(s,ind):
    s = list(s)
    for i in ind:
        if (i < len(s)):
            s[i] = s[i].upper()
        else:
            continue
    return "".join(s)
