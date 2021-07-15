def remove_exclamation_marks(s):
    n = ''
    for x in s:
        if x.isalpha() or x == ' ' or x == ',':
            n += x
    return n
