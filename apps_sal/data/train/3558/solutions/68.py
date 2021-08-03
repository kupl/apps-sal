def capitalize_word(word):
    trueword = list(word)
    s = trueword[0]
    trueword[0] = s.upper()
    return ''.join(trueword)
