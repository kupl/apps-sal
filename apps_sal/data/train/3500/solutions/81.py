def remove_exclamation_marks(s):
    out = ''
    for i in s:
        if i != '!':
            out += i
    return out
