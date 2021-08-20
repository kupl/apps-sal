def remove_exclamation_marks(s):
    new_string = ''
    for e in s:
        if e != '!':
            new_string += e
    return new_string
