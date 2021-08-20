def capitalize_word(word):
    flit = list(word.lower())
    flit[0] = flit[0].upper()
    return ''.join(flit)
