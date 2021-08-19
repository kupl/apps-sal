def replace_exclamation(s):
    vo = 'aeiouAEIOU'
    for a in vo:
        if a in s:
            s = s.replace(a, '!')
    return s
