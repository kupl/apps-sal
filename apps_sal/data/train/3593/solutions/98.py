def capitalize(s, ind):
    return ''.join([value.upper() if index in ind else value for index, value in enumerate(s)])
