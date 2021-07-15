def capitalize_word(word):
    char = 0
    while char < len(word):
        if char == 0:
            word2 = word[char].upper()
        else:
            word2 = word2 + word[char]
        char = char + 1
    return word2
