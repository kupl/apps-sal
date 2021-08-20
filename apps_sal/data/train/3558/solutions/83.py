def capitalize_word(word):
    print(word)
    return ''.join((char.upper() if word.index(char) == 0 else char for char in word))
