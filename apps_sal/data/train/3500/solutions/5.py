def remove_exclamation_marks(s):
    s = list(s)
    for x in s:
        if x == '!':
            s.remove(x)
    for x in s:
        if x == '!':
            s.remove(x)
    for x in s:
        if x == '!':
            s.remove(x)
    return ''.join(s)
