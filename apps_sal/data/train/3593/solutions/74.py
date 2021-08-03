def capitalize(s, ind):
    letters = list(s)
    for i in ind:
        if i >= len(letters):
            break
        letters[i] = letters[i].upper()

    return ''.join(letters)
