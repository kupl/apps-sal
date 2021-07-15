def capitalize(s,ind):
    return ''.join(c.upper() if i in ind else c for i, c in enumerate(s))
