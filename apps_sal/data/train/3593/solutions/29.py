def capitalize(s, ind):
    return ''.join([x.upper() if i in ind else x.lower() for (i, x) in enumerate(s)])
