def remove_exclamation_marks(s):
    """ return s.replace('!', '') """
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s
