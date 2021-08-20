def remove_exclamation_marks(s):
    s1 = []
    for i in s:
        if i != '!':
            s1.append(i)
    return ''.join(s1)
