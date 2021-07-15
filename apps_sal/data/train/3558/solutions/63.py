def capitalize_word(word):
    if len(word) == 1:
        return "".join(char.upper() for char in word)
    else:
        return word[0].upper() + word[1:]
