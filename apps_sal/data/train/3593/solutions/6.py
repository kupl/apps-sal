def capitalize(s,ind):
    return ''.join(j.upper() if i in ind else j for i, j in enumerate(s))
