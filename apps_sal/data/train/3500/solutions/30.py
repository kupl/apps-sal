def remove_exclamation_marks(s):
    a = ""
    for c in s:
        if c != '!':
            a += c
    return a
