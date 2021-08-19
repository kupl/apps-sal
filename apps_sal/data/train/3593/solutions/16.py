def capitalize(s, ind):
    # Iterate over every character 'char' of string 's'.
    # Capitalize the char if its position 'idx' is present
    # in list 'ind'.
    # If it is not, just return the char.
    char_list = [char.upper() if idx in ind else char for (idx, char) in enumerate(s)]
    return ''.join(char_list)
