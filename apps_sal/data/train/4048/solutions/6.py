def pig_latin(word):
    if len(word) < 3:
        return word
    ret = word + word[0] + 'ay'
    return ret[1:]
