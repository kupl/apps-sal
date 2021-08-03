def capitalize(s, ind):
    return ''.join([c, c.upper()][i in ind] for i, c in enumerate(s))
