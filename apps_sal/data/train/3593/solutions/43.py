def capitalize(s, ind):
    return ''.join([i.upper() if loop in ind else i for loop, i in enumerate(s)])
