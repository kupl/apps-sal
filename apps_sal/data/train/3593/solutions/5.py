def capitalize(s,ind):
    for i in ind:
        s = s[:i] + s[i:].capitalize()
    return s
