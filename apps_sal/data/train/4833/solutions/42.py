def replace_exclamation(s):
    v = list('aeiou')
    for i in s:
        if i.lower() in v:
            s = s.replace(i, '!')
    return s
