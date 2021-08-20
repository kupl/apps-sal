def capitalize(s, ind):
    char_list = [char.upper() if idx in ind else char for (idx, char) in enumerate(s)]
    return ''.join(char_list)
