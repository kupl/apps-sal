def capitalize(s, ind):
    s = [*s]
    for n in ind:
        if not n > len(s):
            s[n] = s[n].upper()
    return ''.join(s)
