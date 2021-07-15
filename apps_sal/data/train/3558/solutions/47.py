def capitalize_word(word):
    if len(word) == 1:
        return word.upper()
    return word[0].upper() + word[1:]
