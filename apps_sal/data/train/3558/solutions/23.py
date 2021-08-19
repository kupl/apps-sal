def capitalize_word(word):
    if len(word) >= 2:
        return word[0].upper() + word[1:]
    else:
        return word.upper()
