def capitalize_word(word):
    return capitalize(word)


def capitalize(word):
    s = ''
    for i in range(len(word)):
        if (i == 0):
            s += word[i].upper()
        else:
            s += word[i].lower()
    return s
