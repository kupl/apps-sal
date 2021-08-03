def capitalize(s, ind):
    n = ""
    for i in range(len(s)):
        if i in ind:
            n += s[i].upper()
        else:
            n += s[i]
    return n
