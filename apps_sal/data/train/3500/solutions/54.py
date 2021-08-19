def remove_exclamation_marks(s):
    new_string = ''
    for i in s:
        if i != '!':
            new_string += i
    return new_string
