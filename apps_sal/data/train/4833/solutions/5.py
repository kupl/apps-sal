def replace_exclamation(s):
    for i in 'aeuioAEUIO':
        s = s.replace(i, '!')
    return s
