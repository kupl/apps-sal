def capitalize_word(word):
    for i in word:
        if word[0].lower():
            return word[0].upper() + word[1:]
