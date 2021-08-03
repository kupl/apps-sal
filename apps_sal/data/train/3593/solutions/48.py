def capitalize(s, ind):
    s = list(s)
    for i in ind:
        if i <= len(s) - 1:
            s[i] = s[i].upper()
    return ''.join(s)
