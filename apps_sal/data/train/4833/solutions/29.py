def replace_exclamation(s):
    for c in s:
        if c in 'aeiouAEIOU':
            s = s.replace(c, '!')
    return s
