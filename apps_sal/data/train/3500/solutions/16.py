def remove_exclamation_marks(s):
    s1 = ''
    for i in s:
        if i != '!':
            s1 = s1 + i
    return s1
