def replace_exclamation(s):
    v = 'aeiouAEIOU'
    for i in s:
        if i in v:
            s = s.replace(str(i), '!')
    return s
    # return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
