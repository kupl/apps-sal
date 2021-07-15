def replace_exclamation(s):
    v = 'aeiou'
    for k in s:
        if k.lower() in v:
            s = s.replace(k, '!')
    return s
