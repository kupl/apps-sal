def capitalize_word(word):
    return "".join(char.upper() + word[1:] for char in word[:1])
