def capitalize(s, ind):
    return ''.join([s[i].upper() if i in ind and i < len(s) else s[i] for i in range(len(s))])
