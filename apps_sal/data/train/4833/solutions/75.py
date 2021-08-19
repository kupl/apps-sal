def replace_exclamation(s):
    k = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    t = ''
    for a in s:
        if a in k:
            t += '!'
        else:
            t += a
    return t
