def replace_exclamation(s):
    for i in s:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            s = s.replace(i, '!')
    return s
