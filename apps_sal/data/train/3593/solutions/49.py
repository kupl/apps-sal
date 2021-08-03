def capitalize(s, ind):
    s = list(s)
    return ''.join([s[i].upper() if i in ind else s[i] for i in range(0, len(s))])
