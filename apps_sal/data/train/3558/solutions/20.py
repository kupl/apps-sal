def capitalize_word(word):
    char = [char.upper() for char in word]
    return ''.join(char[0] + word[1:])
