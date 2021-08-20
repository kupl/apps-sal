def pig_latin(word):
    if len(word) <= 3:
        return word
    word = word[1:] + word[0]
    word = word + 'ay'
    return word
