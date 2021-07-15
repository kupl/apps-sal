def capitalize(s,ind):
    return ''.join([m.upper() if i in ind else m for i, m in enumerate(s)])
