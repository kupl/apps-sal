def replace_exclamation(s):
    v = 'aeiouAEIOU'
    for i in s:
        if i in v:
            s = s.replace(str(i), '!')
    return s
