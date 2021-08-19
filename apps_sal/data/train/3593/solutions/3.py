def capitalize(s, ind):
    return ''.join((char.upper() if i in ind else char for (i, char) in enumerate(s)))
