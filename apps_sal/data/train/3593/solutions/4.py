def capitalize(s, ind):
    return ''.join((letter.upper() if index in ind else letter for (index, letter) in enumerate(s)))
