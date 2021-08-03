def capitalize(s, ind):
    return ''.join([s[x].capitalize() if x in ind else s[x] for x in range(len(s))])
