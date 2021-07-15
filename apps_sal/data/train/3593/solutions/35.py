def capitalize(s,ind):
    return ''.join(letter.upper() if i in ind else letter for i, letter in enumerate(s))
