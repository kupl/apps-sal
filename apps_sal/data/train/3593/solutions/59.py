def capitalize(s, ind):
    new_list = []
    for i, letter in enumerate(s):
        if i in ind:
            new_list.append(letter.upper())
        else:
            new_list.append(letter)
    return ''.join(new_list)
