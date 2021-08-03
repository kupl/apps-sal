def capitalize(s, ind):
    new_word = ""
    for idx, val in enumerate(s):
        if idx in ind:
            new_word += val.upper()
        else:
            new_word += val

    return new_word
