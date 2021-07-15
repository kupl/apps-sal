def capitalize(s,ind):
    return ''.join([word.upper() if i in ind else word for i, word in enumerate(s) ])
