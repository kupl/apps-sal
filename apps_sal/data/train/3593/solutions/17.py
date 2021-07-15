def capitalize(s,ind):
    return ''.join([s[i].upper() if i in ind else s[i] for i in range(len(s))])
