def capitalize_word(word):
    if len(word) < 0:
        return word[0].upper()
    char = word[0]
    word = word[1:]
    char = char.upper()
    return char + word
