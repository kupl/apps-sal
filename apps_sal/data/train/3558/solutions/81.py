def capitalize_word(word):
    a = word[0].upper()
    b = slice(1, len(word))
    y = word[b]
    return a + y
